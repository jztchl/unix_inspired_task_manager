from rest_framework import viewsets,response
from task.models import Task
from task.serializers import TaskSerializer,TaskSerializerList
from rest_framework import permissions
from task.task import run_task
import asyncio
import threading
import logging
from task.models import StatusChoices
from task.task import running_tasks

logger = logging.getLogger(__name__)
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
        logger.info(f"Task {task_id} created and added to the queue.")
        return response
    
    def destroy(self, request, *args, **kwargs):
        task= self.get_object()
        this_task = running_tasks.get(task.id)
        if this_task:
            this_task.cancel()
            logger.info(f"Task {task.id} killed.")
            message = f"Task {task.id} killed."
        else:
            logger.info(f"Task {task.id} already completed or killed.")
            message = f"Task {task.id} already completed or killed."
        return response.Response({"detail":message}, status=204)