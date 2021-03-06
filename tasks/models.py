from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(default=' ')
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField(upload_to = 'static/img', null = True)

	def __str__(self):
		return self.title
