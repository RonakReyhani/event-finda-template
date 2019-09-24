from django.db.models.signals import post_save
from .models import customUser, Profile
from django.dispatch import receiver


@receiver(post_save, sender=customUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user=instance)


@receiver(post_save, sender=customUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
