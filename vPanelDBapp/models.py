from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class PermissionGroup(models.Model):  # Used for creating permission groups, to vary access
    permissiongroup = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.permissiongroup


class CustomUserManager(UserManager):
   def get_by_natural_key(self, username):
       case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
       return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
   permissiongroup = models.ForeignKey(PermissionGroup, default=1, on_delete=models.PROTECT)
   objects = CustomUserManager()


class HUGOgene(models.Model):
    ensemblGeneID = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=10)
    locationSortable = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Panel(models.Model):
    panelName = models.CharField(max_length=20, blank=True, null=True, unique=True)
    panelID = models.CharField(max_length=20, blank=True, null=True)
    panelVersion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)

    def __str__(self):
        return self.panelName


class Subpanel(models.Model):
    subpanelName = models.CharField(max_length=20, blank=True, null=True, unique=True)
    subpanelID = models.CharField(max_length=20, blank=True, null=True)
    subpanelVersion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)
    panel = models.ForeignKey(Panel, blank=True, null=True)

    def __str__(self):
        return self.subpanelName