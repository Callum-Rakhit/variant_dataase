from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	Panel_Name = models.CharField(max_length=200)
	genes = models.TextField()
	subpanels = models.NullBooleanField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Panel_Name

class Panel(models.Model):
    PanelName = models.CharField(max_length=30, unique=True)
    Notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.PanelName

class Gene(models.Model):
    Panel = models.ForeignKey(Panel, null=True, blank=True)
    GeneName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.GeneName
