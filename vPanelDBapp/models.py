from django.db import models


class HUGOgene(models.Model):
    HUGO_Gene_ID = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.HUGO_Gene_ID


class Panel(models.Model):
    Panel_Name = models.CharField(max_length=200, blank=True, null=True)
    Panel_ID = models.TextField(max_length=200, blank=True, null=True)
    Panel_Version = models.TextField(max_length=200, blank=True, null=True)
    Username = models.TextField(max_length=200, blank=True, null=True)
    HUGOgene = models.ForeignKey(HUGOgene, blank=True, null=True)

    def __str__(self):
        return self.Panel_Name


class Subpanel(models.Model):
    Subpanel_Name = models.CharField(max_length=200, blank=True, null=True)
    Subpanel_ID = models.TextField(max_length=200, blank=True, null=True)
    Subpanel_Version = models.TextField(max_length=200, blank=True, null=True)
    Username = models.TextField(max_length=200, blank=True, null=True)
    HUGOgene = models.ForeignKey(HUGOgene, blank=True, null=True)
    Panel = models.ForeignKey(Panel, blank=True, null=True)

    def __str__(self):
        return self.Subpanel_Name