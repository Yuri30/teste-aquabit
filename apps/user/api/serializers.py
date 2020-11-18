from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id','first_name','username', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user