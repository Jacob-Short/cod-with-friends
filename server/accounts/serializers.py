
from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from rest_framework.views import APIView

from accounts.models import UserAccount

class UserAccountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'picture',
            'bio',
            'display_name',
        ]



class CreateUserAccountSerializer(APIView):
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'picture',
            'bio',
            'display_name',
        ]