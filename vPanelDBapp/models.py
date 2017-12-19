from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class PermissionGroup(models.Model):  # Used for creating permission groups, to vary access
    permissiongroup = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.permissiongroup


class CustomUserManager(UserManager):  # UserManager is a premade Django model
   def get_by_natural_key(self, username):
       case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
       return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):  # AbstractManager is a premade Django model
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
    DIAGNOSTIC = 'DI'
    RESEARCH = 'RE'
    panelType = (
        (DIAGNOSTIC, 'Diagnostic'),
        (RESEARCH, 'Research'),
    )
    panelTypes = models.CharField(
        max_length=2,
        choices=panelType,
        default=DIAGNOSTIC,
    )

    def __str__(self):
        return self.panelName



    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevUsername=self.username)

    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevPanelName=self.panelName)

    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevPanelID=self.panelID)

    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevPanelVersion=self.panelVersion)

    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevGene=self.gene)

    def save(self, force_insert=False, force_update=False, using=None):
        super(Panel, self).save()
        LogChanges.objects.create(prevPanelTypes=self.panelTypes)

'''

class LogChanges(models.Model):  # Table to save changes to panels
    createdAt = models.DateTimeField(auto_now_add=True)
    prevUsername = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.panelName

    def save(self):
        super(Panel, self).save()
        LogChanges.objects.create(prevUsername=self.username)

    def __str__(self):
        return self.prevUsername

'''

    prevPanelName = models.CharField(max_length=20, blank=True, null=True, unique=True)
    prevPanelID = models.CharField(max_length=20, blank=True, null=True)
    prevPanelVersion = models.IntegerField(blank=True, null=True)
    prevGene = models.ManyToManyField(HUGOgene, blank=True)
    DIAGNOSTIC = 'DI'
    RESEARCH = 'RE'
    panelType = (
        (DIAGNOSTIC, 'Diagnostic'),
        (RESEARCH, 'Research'),
    )
    prevPanelTypes = models.CharField(max_length=2,
                                      choices = panelType,
                                      default = DIAGNOSTIC,
                                      )

'''



class Subpanel(models.Model):
    subpanelName = models.CharField(max_length=20, blank=True, null=True, unique=True)
    subpanelID = models.CharField(max_length=20, blank=True, null=True)
    subpanelVersion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)
    panel = models.ForeignKey(Panel, blank=True, null=True)

    def __str__(self):
        return self.subpanelName