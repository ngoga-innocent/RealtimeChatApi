from django.shortcuts import render,redirect
from .models import Room,Message
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import RoomSerializer,MessageSerializer
# Create your views here.
def HomeView(request, *args, **kwargs):
    if request.method == 'POST':
        username=request.POST['username']
        room=request.POST['room']
        try:
            existing_room=Room.objects.get(name__icontains=room)
            return redirect('room',room_name=existing_room,username=username)
        except Room.DoesNotExist:
            new_room=Room.objects.create(name=room)
            new_room.save()
            return redirect('room',room_name=new_room.name,username=username)
    return render(request, 'home.html')
def RoomView(request,room_name,username, *args, **kwargs):
    existing_room=Room.objects.get(name__icontains=room_name)
    messages=Message.objects.filter(room=existing_room)
    
    context={
        'room_name': existing_room.name,
        'messages': messages,
        'username': username  # new
    }
    return render(request, 'room.html',context)
class RoomViewAPI(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class MessageView(APIView):
    def get(self, request,room_id=None, *args, **kwargs):
            room=Room.objects.get(id=room_id)
            messages=Message.objects.filter(room=room)
            serializer=MessageSerializer(messages, many=True)
            return Response({'messages':serializer.data})