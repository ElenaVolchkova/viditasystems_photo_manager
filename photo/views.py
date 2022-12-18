from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, generics, permissions, status

from .models import Photo
from .serializers import UserSerializer, GroupSerializer, PhotoSerializer, PhotoDetailSerializer
from .service import PhotoFilter
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PhotoAPIList(generics.ListCreateAPIView):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, )
    filter_class = PhotoFilter
    search_fields = ['$people_name']
    filterset_fields = ['date', 'people_name', 'location_name', 'lon', 'lat']
    permission_classes = [permissions.IsAuthenticated]


class PhotoDetailView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows photo to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhotoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)