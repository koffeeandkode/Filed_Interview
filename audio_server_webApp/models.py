import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class song(models.Model):

    id = models.AutoField(primary_key=True) 
    song_name = models.CharField(max_length=100, blank=False, null=False)
    duration_in_sec = models.IntegerField(blank=False, null=False, default=0)
    upload_time = models.DateTimeField(blank=False, null=False, default = datetime.datetime.utcnow())



    def __str__(self):
        return self.song_name

    def was_published_recently(self):
        return self.upload_time >= timezone.now() - datetime.timedelta(days=1)


class podcast(models.Model):

	id = models.AutoField(primary_key=True)
	podcast_name = models.CharField(max_length=100, blank=False, null=False)
	duration_in_sec = models.DurationField(blank=False, null=False)
	upload_time = models.DateTimeField(blank=False, null=False)
	host = models.CharField(max_length=100, blank=False, null=False)

	def __str__(self):
		return self.podcast_name

	def was_published_recently(self):
		return self.upload_time >= timezone.now() - datetime.timedelta(days=1)

class audiobook(models.Model):

	id = models.AutoField(primary_key=True)
	audiobook_name = models.CharField(max_length=100, blank=False, null=False)
	author_name = models.CharField(max_length=100, blank=False, null=False)
	narrator = models.CharField(max_length=100, blank=False, null=False)
	duration_in_sec = models.DurationField(blank=False, null=False)
	upload_time = models.DateTimeField(blank=False, null=False)

	def __str__(self):
		return self.audiobook_name

	def was_published_recently(self):
		return self.upload_time >= timezone.now() - datetime.timedelta(days=1)
