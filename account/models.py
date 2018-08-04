from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class user_profile(models.Model):
    #sets attributes of a user_profile object
    #information that can be accessed later and display on users profiles
    user = models.OneToOneField(User, on_delete="")
    description = models.CharField(max_length=140, default='')
    city = models.CharField(max_length=64, default='')
    grade = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    #if the User object being passed has been created
    if kwargs['created']:
        #create a user_profile object that corresponds
        u_p = user_profile.objects.create(user=kwargs['instance'])

#when this model object is saved, run function create_profile and pass in
#information about the user
post_save.connect(create_profile, sender=User)

