from rest_framework import serializers
from .models import Company, PostComment, CompanyComment, Post, User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'


class CompanyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyComment
        fields = '__all__'
