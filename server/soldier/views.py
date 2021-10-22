from django.shortcuts import render

# rest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# serializers
from soldier.serializers import SoldierSerializer

# models 
from soldier.models import Soldier


class ManufacturerViewSet(ModelViewSet):
    '''get all soliders'''
    serializer_class = SoldierSerializer
    queryset = Soldier.objects.all()
