from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    
        return code

# Create your models here.
# Basically a model is a table from a generic database, in this case it would be about rooms, hosts, etc

class Room(models.Model):
    # what would we need to have a room
    code = models.CharField(max_length=8,default="",unique=True) # code unique for each room with max length 8 
    host = models.CharField(max_length=50,unique=True) # each room can have only one host
    guest_can_pause = models.BooleanField(null=False,default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

