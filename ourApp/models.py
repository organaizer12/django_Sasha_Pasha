from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length = 250)
	text = models.TextField()
	created_date = models.DateTimeField(
		blank = True, null = True)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()	
		self.save()

	def __str__(self):
		return self.title

class News(models.Model):
	source = models.CharField(max_length = 250)
	header = models.CharField(max_length = 250)
	viewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	def __str__(self):
		return 'First news from %s: %s' % (self.source, self.header)