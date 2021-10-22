from django.shortcuts import render

# rest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# serializers
from weapons.serializers import WeaponSerializer

# models 
from weapons.models import Weapon


class ManufacturerViewSet(ModelViewSet):
    '''get all weapons'''
    serializer_class = WeaponSerializer
    queryset = Weapon.objects.all()
