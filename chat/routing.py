from django.urls import path
from .consumers import ChatConsumer,ChatApiConsumer
wsPattern=[
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    path('ws/chatapi/<int:room_id>/', ChatApiConsumer.as_asgi()),  # for API
]