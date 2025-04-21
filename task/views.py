from rest_framework import viewsets
from task.models import Task
from task.serializers import TaskSerializer,TaskSerializerList

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def get_serializer_class(self):
        if self.action =="list":
            return TaskSerializerList
        return super().get_serializer_class()
    
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset
    
    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise Http404("Task not found")
        return obj