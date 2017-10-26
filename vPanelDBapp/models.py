from django.db import models


class NGSPanel(models.Model):
    author = models.ForeignKey('auth.User')
    NGS_Panel_Name = models.CharField(max_length=200)
    Transcript_IDs = models.TextField(blank=True, null=True)
    Virtual_Panels = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return self.NGS_Panel_Name


class HUGOgene(models.Model):
    HUGO_Gene_ID = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.HUGO_Gene_ID


class NewSubpanel(models.Model):
    author = models.ForeignKey('auth.User')
    Subpanel_Name = models.CharField(max_length=200)
    Subpanel_IDs = models.TextField()
    Transcript_IDs = models.TextField(blank=True, null=True)
    Virtual_Panels = models.NullBooleanField(blank=True, null=True)
    HUGOgene = models.ForeignKey(HUGOgene, blank=True, null=True)

    def __str__(self):
        return self.Subpanel_Name