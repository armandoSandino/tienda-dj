#
from rest_framework import serializers

class LoginSocialSerializer(serializers.Serializer):

    el_token = serializers.CharField(
        required = True
    ) 