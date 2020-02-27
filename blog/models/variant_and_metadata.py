from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Variant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    age	= models.PositiveIntegerField()
    proband_affected = models.CharField(max_length=80)
    relatives = models.CharField(max_length=80)
    stage = models.PositiveIntegerField()
    description = models.CharField(max_length=80)
    sequencer = models.CharField(max_length=80)
    variant_cDNA = models.CharField(max_length=80)
    variant_protein = models.CharField(max_length=80)
    variant_genome = models.CharField(max_length=80)
    pathogenicity_code = models.CharField(max_length=80)
    evidence = models.CharField(max_length=80)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:variant', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title, username=self.user.username)
