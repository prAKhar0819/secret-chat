from django.urls import re_path
from chat.consumers import ChatConsumer

# Define websocket_urlpatterns to be used in asgi.py
websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),  # WebSocket URL for chat
]

