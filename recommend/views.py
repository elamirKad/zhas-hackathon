from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recommend.models import Cosmetics
from recommend.serializers import CosmeticsSerializer


class CosmeticsViewSet(viewsets.ModelViewSet):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmeticsSerializer