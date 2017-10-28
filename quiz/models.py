from django.db import models
from django.contrib.auth.models import User

class Selection(models.Model):
	user = models.ForeignKey(User)
	image_url = models.CharField(max_length=1000)
	image_category = models.CharField(max_length=200)
	date = models.DateTimeField('date', auto_now_add=True, blank=True, null=True)

	def __str__(self):              
		return str(self.user.username)

