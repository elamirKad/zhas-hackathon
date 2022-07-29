from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from recommend.models import Cosmetics
from recommend.serializers import CosmeticsSerializer
from recommend_engine import Recommendation


class CosmeticsViewSet(viewsets.ModelViewSet):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmeticsSerializer

class RecommendAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})
        try:
            rec = Recommendation()
            lst = []
            for id, percent in rec.get_recommendation(pk):
                lst.append(id)
            objects = Cosmetics.objects.filter(id__in=lst)
            return Response({'cosmetics': CosmeticsSerializer(objects, many=True).data})
        except:
            return Response({"error": "Object does not exists"})
