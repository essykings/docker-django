from rest_framework import serializers
from tasks.models import Task


class tasksSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description','date')
