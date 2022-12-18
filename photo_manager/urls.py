"""photo_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from photo.views import UserViewSet, GroupViewSet, PhotoAPIDestroy, PhotoDetailView, PhotoAPIList, \
    RegistrUserView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('registr/', RegistrUserView.as_view(), name='registr'),
    path('admin/', admin.site.urls),
    path('api/v1/photo_delete/<int:pk>', PhotoAPIDestroy.as_view()),
    path('api/v1/photos/<int:pk>', PhotoDetailView.as_view()),
    path('api/v1/photos/', PhotoAPIList.as_view()),
]
