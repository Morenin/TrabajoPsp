from rest_framework import serializers
from nucleo.user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ['first_name','last_name','Dni']