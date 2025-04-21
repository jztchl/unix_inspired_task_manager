from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'created_at', 'updated_at', 'completed_at']