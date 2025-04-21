from rest_framework import viewsets
from task.models import Task
from task.serializers import TaskSerializer,TaskSerializerList
from rest_framework import permissions
from task.task import run_task
import asyncio
import threading
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= [permissions.IsAuthenticated,]
    
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
    
    def create(self, request, *args, **kwargs):
        response=super().create(request, *args, **kwargs)
        task_id = response.data['id']
        threading.Thread(target=lambda: asyncio.run(run_task(task_id))).start()
        return response