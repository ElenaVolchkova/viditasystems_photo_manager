from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, generics
from rest_framework import permissions

from .models import Photo
from .serializers import UserSerializer, GroupSerializer, PhotoSerializer, PhotoDetailSerializer
from .service import PhotoFilter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()#.order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()#.order_by('-date_joined')
    serializer_class = PhotoSerializer
    # filter_backends = (DjangoFilterBackend, )
    # filter_class = PhotoFilter
    # permission_classes = [permissions.IsAuthenticated]


class PhotoAPIList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()  # .order_by('-date_joined')
    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, )
    filter_class = PhotoFilter
    search_fields = ['$people_name']
    filterset_fields = ['date', 'people_name', 'location_name', 'lon', 'lat']


class PhotoDetailView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows photo to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class PhotoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    # permission_classes = (IsOwnerOrReadOnly,)