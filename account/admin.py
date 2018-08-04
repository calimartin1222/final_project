from django.contrib import admin
from account.models import user_profile

#adds the model user_profile to admin page so it can be manipulated
admin.site.register(user_profile)