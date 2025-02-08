from django.urls import path
from .import views
urlpatterns=[
    path('', views.HomeView, name='home'),
    path('api/rooms/', views.RoomViewAPI.as_view(), name='api-rooms'),
    path('api/rooms/<int:room_id>/messages/', views.MessageView.as_view(), name='api-messages'), 
    path('room/<str:room_name>/<str:username>', views.RoomView, name='room'),
]