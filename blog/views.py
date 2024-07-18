from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from .models import *
from .serializer import PostSerializer, CustomUserSerializer, PostCommentSerializer, CompanyCommentSerializer


class PostListAPIView(ListAPIView, LoginRequiredMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCommentViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyCommentViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = CompanyComment.objects.all()
    serializer_class = CompanyCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
