from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        print("Profile created")
        return profile

def my_callback(sender=MyUser, **kwargs):
    print("User and its profile created!")
        