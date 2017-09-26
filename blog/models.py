from django.db import models
from django.utils import timezone

class NGSPanel(models.Model):
	author = models.ForeignKey('auth.User')
	NGS_Panel_Name = models.CharField(max_length=200)
	Gene_IDs = models.TextField()
	Transcript_IDs = models.TextField(blank=True, null=True)
	Virtual_Panels = models.NullBooleanField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.NGS_Panel_Name

class NewGene(models.Model):
	author = models.ForeignKey('auth.User')
	Gene_Name = models.CharField(max_length=200)
	Gene_IDs = models.TextField()
	Transcript_IDs = models.TextField(blank=True, null=True)
	Virtual_Panels = models.NullBooleanField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Gene_Name