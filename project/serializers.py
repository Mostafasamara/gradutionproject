from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Project , Task , Group , UserProfile

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    # groups = serializers.HyperlinkedRelatedField(many=True, view_name='groups', read_only=True)

    class Meta:
        model = Project
        fields = ['url', 'id','owner', 'title','created','tasks','group']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # member = serializers.HyperlinkedIdentityField(view_name='members')
    class Meta:
        model = Task
        fields = ['url','project_id', 'id','owner','title','start','end','desc','project','status','member']




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Group
        fields = ('url','title','owner','member','created','active',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)
    # tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    # group = serializers.HyperlinkedRelatedField(many=True, view_name='groups_owner', read_only=True)
    # member = serializers.ReadOnlyField(source='member.username')
    # photo = serializers.ImageField()

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = ['url','id','username','password','first_name', 'last_name', 'email']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
