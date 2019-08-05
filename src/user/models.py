from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class user_profile(models.Model):
	# user_name = models.CharField(max_length=50) #max_length = required
	# email = models.CharField(max_length=60) 
	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')	
	contact_number = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=8)
	# password1 = models.CharField(max_length=20)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		user_profile.objects.create(user=instance)
	instance.profile.save()
