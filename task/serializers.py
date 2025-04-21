from rest_framework import serializers
from task.models import Task
class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'completed_at']
    
    def create(self, validated_data):
        validated_data['user']=self.context['user']
        return super().create(validated_data)
    

class TaskSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','status']