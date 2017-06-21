from app.models import User
from django.db.models.signals import (pre_save, post_save)
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def create_user_values(sender, instance, *args, **kwargs):
    if (instance.pk == None):
        instance.generate_token()
        instance.hash_password()


@receiver(post_save, sender=User)
def update_user_id(sender, instance, created, *args, **kwards):
    if created:
        instance.assign_user_id()

