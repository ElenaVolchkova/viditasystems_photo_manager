from django.contrib.auth.models import User, Group
from rest_framework import serializers

from photo.models import Photo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image')
        # fields = "__all__"

class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"