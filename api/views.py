from tasks.models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
