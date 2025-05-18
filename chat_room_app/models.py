from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Customers(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    mobile_no=models.BigIntegerField()
    status=models.CharField(max_length=50)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)

class Chatroom(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=70)
    created_by=models.IntegerField(null=True,blank=True)
    valid_till=models.DateField(null=True,blank=True)
    create_Date=models.DateTimeField(default=timezone.now)
    updated_Date=models.DateTimeField(auto_now=True)



class Chat(models.Model):
    chatroom_id=models.ForeignKey(to=Chatroom,on_delete=models.CASCADE)
    client_id=models.ForeignKey(to=Customers,on_delete=models.CASCADE)
    message=models.CharField(max_length=50)
    sender=models.CharField(max_length=50)
    message_Type=models.CharField(max_length=100)
    attechment=models.FileField(upload_to='attechment/',null=True,blank=True)
    create_Date=models.DateTimeField(default=timezone.now)
    updated_Date=models.DateTimeField(auto_now=True)

