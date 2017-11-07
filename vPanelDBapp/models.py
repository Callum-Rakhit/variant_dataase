from django.db import models
from smart_selects.db_fields import ChainedForeignKey, \
    ChainedManyToManyField, GroupedForeignKey


class HUGOgene(models.Model):
    ensemblGeneID = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=10)
    locationSortable = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Panel(models.Model):
    panelName = models.CharField(max_length=20, blank=True, null=True)
    panelID = models.CharField(max_length=20, blank=True, null=True)
    panelVersion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)

    def __str__(self):
        return self.panelName


class Subpanel(models.Model):
    subpanelName = models.CharField(max_length=20, blank=True, null=True)
    subpanelID = models.CharField(max_length=20, blank=True, null=True)
    subpanelVersion = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)
    panel = models.ForeignKey(Panel, blank=True, null=True)

    def __str__(self):
        return self.subpanelName
