from rest_framework import serializers
from .models import Task


class TaskSetiallizar(serializers.ModelSerializer):
    class Meta: 
        model = Task
        #fields = ('id', 'title', 'description', 'done')
        fields = '__all__'