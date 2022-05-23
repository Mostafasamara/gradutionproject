from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import chain
from django_filters import rest_framework as filters
from rest_framework import mixins, generics
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Project , Task , Group , UserProfile
from .permissions import IsOwnerOrReadOnly ,  IsMember
from .serializers import ProjectSerializer, UserSerializer,TaskSerializer , GroupSerializer,UserProfileSerializer
from rest_framework.decorators import action
from django.db.models import Q
# from itertools import chain
from functools import partial

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
    permission_classes = [
        permissions.IsAuthenticated,
        # IsMember,
         ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ('owner','member',)
    # def get_queryset(self):
    #     queryset = self.queryset
    #     q1 = queryset.filter(owner = self.request.user)
    #     return q1
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated,
          IsOwnerOrReadOnly,]
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ('owner','member',)
    # lookup_field = 'owner'


    # def get_queryset(self):
    #     queryset = Group.objects.filter(member=self.request.user)
    #
    #
    #     return  queryset

            # return queryset.filter(member=self.request.user)
        # return owner and members

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user,

        )


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.AllowAny , )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated , )
