from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
from channels.db import database_sync_to_async
import json
from .models import Message,Room
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name,self.channel_name)
        await self.accept()
    async def receive(self, text_data):
        data=json.loads(text_data)
        event={
            "type":"send_message",
            "message":data
        }
        await self.channel_layer.group_send(self.room_name,event) 
    async def send_message(self,event):
        message=event['message']
        await self.create_message(data=message)
        response={
            "sender":message["sender"],
            "message":message["message"]
        }    
        await self.send(json.dumps({"message":response}))
    @database_sync_to_async
    def create_message(self,data):
        message=data['message']
        sender=data['sender']
        room_name=data['room_name']
        room=Room.objects.get(name=room_name)
        message=Message.objects.create(message=message,room=room,sender=sender)
        print(message)   
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name,self.channel_name) 
        await self.close(code)
class ChatApiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id=f"{self.scope['url_route']['kwargs']['room_id']}"
        await self.channel_layer.group_add(self.room_id,self.channel_name)
        await self.accept() 
    async def receive(self, text_data=None):
        message=json.loads(text_data)
        print(message.get('message'))
        event={
            "type":"send_group_message",
            "message":message
        }    
        await self.channel_layer.group_send(self.room_id,event)
    async def send_group_message(self,message):
        await self.create_databaseMessage(data=message)
        print(message)
        await self.send(json.dumps({"message":message}))
        
    @database_sync_to_async
    def create_databaseMessage(self,data):
        print("dta to save",data['message']['message'])
        message=data['message']['message']
        sender=data['message']['message']
        # print(message)
        try:
            room=Room.objects.get(id=self.room_id)
        except Room.DoesNotExist:
            room=Room.objects.create(name=sender)
        message=Message.objects.create(room=room, sender=sender, message=message)
        print(message)                
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_id,self.channel_name) 
        await self.close(code)            