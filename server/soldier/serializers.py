
from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from rest_framework.views import APIView

from soldier.models import Soldier

class SoldierSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Soldier
        fields = [
            'gamer_tag',
            'email',
            'picture',
            'bio',
        ]


class CreateSoldierSerializer(APIView):
    class Meta:
        model = Soldier
        fields = [
            'gamer_tag',
            'email',
            'picture',
            'bio',
        ]