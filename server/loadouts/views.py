from django.shortcuts import render

# rest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# serializers
from loadouts.serializers import LoadoutSerializer

# models 
from loadouts.models import Loadout



class ManufacturerViewSet(ModelViewSet):
    '''get all loadouts'''
    serializer_class = LoadoutSerializer
    queryset = Loadout.objects.all()
