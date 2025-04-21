from rest_framework import serializers
from user.models import User
import re
import logging
logger = logging.getLogger(__name__)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self,value):
        if not re.match(r'^[A-Za-z0-9_]+$', value):
            raise serializers.ValidationError("Username must be alphanumeric and can include underscores only.")
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
        
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        logger.info(f"User {user.username} created successfully.")
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)

        instance.save()
        logger.info(f"User {instance.username} updated successfully.")
        return instance