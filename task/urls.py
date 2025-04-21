from django.urls import path
from rest_framework import routers
from task.views import TaskViewSet
from django.urls import include

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
]