from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete="")
    description = models.CharField(max_length=140, default='')
    city = models.CharField(max_length=64, default='')
    grade = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        u_p = user_profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

