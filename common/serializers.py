from common.models import *
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active',
                  'is_admin', 'is_staff', 'date_joined', 'role', 'profile_pic', ]
