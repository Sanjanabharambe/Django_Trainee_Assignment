import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(" Signal handler thread ID:", threading.get_ident())


print("Caller thread ID:", threading.get_ident())
MyModel.objects.create(name="Sanjana")