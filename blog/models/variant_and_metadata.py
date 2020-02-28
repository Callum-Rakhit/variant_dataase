from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Variant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_field = models.CharField(max_length=80, blank = False, null = False)
    age_field	= models.PositiveIntegerField(blank = False, null = False)
    is_proband = models.CharField(max_length=80, blank = False, null = False)
    aff_relative = models.CharField(max_length=80, blank = False, null = False)
    stage_field = models.PositiveIntegerField(blank = False, null = False)
    desc_field = models.CharField(max_length=80, blank = False, null = False)
    sequencer = models.CharField(max_length=80, blank = False, null = False)
    variant_cDNA = models.CharField(max_length=80, blank = False, null = False)
    variant_protein = models.CharField(max_length=80, blank = False, null = False)
    variant_genome = models.CharField(max_length=80, blank = False, null = False)
    pathogenicity_code = models.CharField(max_length=80, blank = False, null = False)
    evidence = models.CharField(max_length=80, blank = False, null = False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:variant', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title, username=self.user.username)
