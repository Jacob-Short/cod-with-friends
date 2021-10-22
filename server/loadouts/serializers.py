
from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from rest_framework.views import APIView

from loadouts.models import Loadout

class LoadoutSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Loadout
        fields = [
            'name',
            'weapons',
            'picture',
            'user_account',
        ]



class CreateLoadoutSerializer(APIView):
    class Meta:
        model = Loadout
        fields = [
            'name',
            'weapons',
            'picture',
            'user_account',
        ]