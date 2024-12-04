from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from users.models import UserIcon
User = get_user_model()
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=32, unique=True)
    avatar = models.ImageField(upload_to="chats/rooms/", blank=True, null=True)


    def __str__(self):
        return self.title
    

class Room(models.Model):
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="category_rooms")
    name = models.CharField(max_length=32, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User, blank=True, related_name="user_rooms")
    required_decency = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    description = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="owner_rooms")
    avatar = models.ImageField(upload_to="chats/rooms/", default="default.jpg")
    icon = models.ForeignKey(UserIcon, on_delete=models.CASCADE, default=1, related_name="icon_room")


    def __str__(self):
        return self.name

class Messages(models.Model):
    text = models.TextField()
    time_send = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="room_messages")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_messages")
    

    def __str__(self):
        return self.text
    
class Report(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reports")