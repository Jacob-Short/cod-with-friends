
from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from rest_framework.views import APIView

from weapons.models import Weapon, Attachment

class WeaponSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Weapon
        fields = [
            'name',
            'attachments',
            'picture',
            'details',
        ]


class CreateWeaponSerializer(APIView):
    class Meta:
        model = Weapon
        fields = [
            'name',
            'attachments',
            'picture',
            'details',
        ]


class AttachmentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            'name',
            'picture',
            'details',
        ]


class CreateAttachmentSerializer(APIView):
    class Meta:
        model = Attachment
        fields = [
            'name',
            'picture',
            'details',
        ]



