


from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password1', 'first_name', 'last_name', 'email')
        write_only_fields = ('password1',)
    
        def create(self, validated_data):
            user = User(email=validated_data['email'], username=validated_data['username'])
            user.set_password(validated_data['password1'])
            user.save()
            return user


