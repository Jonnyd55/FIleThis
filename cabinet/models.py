from django.db import models
from django.db import models

from taggit.managers import TaggableManager

# Create your models here.
class File(models.Model):
	provider_url = models.CharField(null=True, blank=True, max_length=500)
	provider_name = models.CharField(max_length = 128, null=True, blank=True)
	title = models.CharField(max_length = 300, null=True, blank=True)
	bookmark_date = models.DateField(auto_now=True, null=True, blank=True)
	pub_date = models.DateField(null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	thumbnail = models.CharField(max_length = 500, null=True, blank=True)
	summary = models.TextField(null=True, blank=True)
	author = models.CharField(max_length = 400, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	tags = TaggableManager()

	def __str__(self):
		return self.title
