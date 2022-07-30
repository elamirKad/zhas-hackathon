from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from recommend.models import Cosmetics
from recommend.serializers import CosmeticsSerializer
from recommend_engine import Recommendation
from django_filters import rest_framework as filters


class CosmeticsFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')


class CosmeticsViewSet(viewsets.ModelViewSet):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmeticsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CosmeticsFilter

class RecommendAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})
        try:
            amount = kwargs.get("amount", None)
            temp = str(pk)
            pk_list = temp.split(".")
            rec = Recommendation()
            lst = []
            for p in pk_list:
                if not amount:
                    for id, percent in rec.get_recommendation(int(p)):
                        lst.append(id)
                else:
                    for id, percent in rec.get_recommendation(int(p), amount):
                        lst.append(id)

            objects = Cosmetics.objects.filter(id__in=lst)
            return Response({'cosmetics': CosmeticsSerializer(objects, many=True).data})
        except:
            return Response({"error": "Object does not exists"})
