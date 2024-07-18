from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'post-comment', PostCommentViewSet)
router.register(r'company-comment', CompanyCommentViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListAPIView.as_view(), name='posts'),
]