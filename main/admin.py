from django.contrib import admin

# Register your models here.
from .models import GalleryCategory,Profile,GalleryImage,EmailSubscription,Event,Booking

admin.site.register(Profile)
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(EmailSubscription)




