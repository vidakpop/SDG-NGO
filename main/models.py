from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    address = models.TextField(default='',blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=1000,blank=True, null=True,default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000,blank=True, null=True,default='')
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    #@property
    def is_upcoming(self):
        return self.date >= timezone.now()

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.profile} for {self.event.title}"
class EmailSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.email