from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TaskSetiallizar
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSetiallizar
    queryset = Task.objects.all()