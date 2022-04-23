from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project , Task


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = Project
        fields = ['url', 'id','owner', 'title','created','tasks']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    projects = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = Task
        fields = ['url', 'id','owner','project', 'title','start','end','desc','projects']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'projects','tasks']
