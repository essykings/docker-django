from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Task


# Create your views here.


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = tasksSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = tasksSerializer