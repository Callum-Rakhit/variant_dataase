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
    Panel_Name = models.CharField(max_length=20, blank=True, null=True)
    Panel_ID = models.CharField(max_length=20, blank=True, null=True)
    Panel_Version = models.IntegerField(blank=True, null=True)
    Username = models.CharField(max_length=20, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True, null=True)

    def __str__(self):
        return self.Panel_Name


class Subpanel(models.Model):
    Subpanel_Name = models.CharField(max_length=20, blank=True, null=True)
    Subpanel_ID = models.CharField(max_length=20, blank=True, null=True)
    Subpanel_Version = models.IntegerField(blank=True, null=True)
    Username = models.CharField(max_length=200, blank=True, null=True)
    gene = models.ManyToManyField(HUGOgene, blank=True)
    panel = ChainedManyToManyField(
        "Panel",
        horizontal=True,
        verbose_name='Subpanel Parent',
        chained_field="gene",
        chained_model_field="gene",
        auto_choose=True, blank=True, null=True)

    def __str__(self):
        return self.Subpanel_Name