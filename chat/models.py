from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    # profile = models.ImageField(upload_to='Room')
    def __str__(self):
        return self.name
class Message(models.Model):
    message=models.TextField()
    sender=models.CharField(max_length=200)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.sender}: {self.message[:20]}..."