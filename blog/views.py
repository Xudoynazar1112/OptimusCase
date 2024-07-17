from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions

from .models import *
from .serializer import PostSerializer, CustomUserSerializer


class PostViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
