from rest_framework import serializers
from task.models import Task
from django.utils import timezone
class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'completed_at']
    
    def create(self, validated_data):
        validated_data['user']=self.context['user']
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = timezone.localtime(instance.created_at).strftime('%Y-%m-%d %H:%M:%S')
        representation['updated_at'] = timezone.localtime(instance.updated_at).strftime('%Y-%m-%d %H:%M:%S')
        representation['status'] = instance.status
        if instance.completed_at:
            representation['completed_at'] = timezone.localtime(instance.completed_at).strftime('%Y-%m-%d %H:%M:%S')
        else:
            representation['completed_at'] = None
        return representation
    

class TaskSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','status']