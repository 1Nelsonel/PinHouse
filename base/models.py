from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from  embed_video.fields  import  EmbedVideoField


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200, null=True)
   


    def __str__(self):
        return self.name[0:50]

class Property(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    houseimage1 = models.ImageField(upload_to='media', null=True)
    livingroomimage2 = models.ImageField(upload_to='media', null=True)
    kitchenimage3 = models.ImageField(upload_to='media', null=True)
    bathroomimage4 = models.ImageField(upload_to='media', null=True)
    bedroomimage5 = models.ImageField(upload_to='media', null=True)
    location = models.CharField(max_length=250,default='Nairobi', null=True)
    price = models.IntegerField(default='0')
    baths = models.IntegerField(default='0', null=True)
    rooms = models.IntegerField(default='0',null=True)
    garages = models.IntegerField(default='0',null=True)
    amenity1 = models.CharField(max_length=200, default='24/7 security/cctv cameras.', blank=True)
    amenity2 = models.CharField(max_length=200, default='silent estate', blank=True)
    amenity3 = models.CharField(max_length=200, default='Backup generator', blank=True)
    amenity4 = models.CharField(max_length=200, default='Kindergatten availableKindergatten available', blank=True)
    amenity5 = models.CharField(max_length=200, default='Supermarket', blank=True)
    amenity6 = models.CharField(max_length=200, default='Reserved water', blank=True)
    videolink = EmbedVideoField(default='https://player.vimeo.com/video/73221098')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name[0:50]

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

