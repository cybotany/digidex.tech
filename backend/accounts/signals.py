from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    """
    Automatically sets up a new user when they are created by calling setup().
    """
    if created:
        instance.setup()