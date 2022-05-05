from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from itertools import chain
from .models import Project , Task , Group
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer, UserSerializer,TaskSerializer , GroupSerializer
from rest_framework.decorators import action
from django.db.models import Q
from itertools import chain

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (
        permissions.IsAuthenticated, )

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set


    def perform_create(self, serializer):
        data = self.request.data
        project = None
        if project in data:
            project = data['project.title']
        serializer.save(owner=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_owner(self):
        queryset = self.queryset
        owner = queryset.filter(owner = self.request.user)
        return owner

    def get_member(self):
        queryset = self.queryset
        member = queryset.filter(member = self.request.user)
        return member

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated , )

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter( username=self.request.user)

        return query_set
