from django.urls import path
from .views import NotificationView, NotificationConsumer


urlpatterns = [
    path('', NotificationView.as_view(), name='notification'),
]

websocket_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
]