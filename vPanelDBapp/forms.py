from django import forms
from .models import NGSPanel, NewGene, HUGOgene

class NGSPanelForm(forms.ModelForm):

    class Meta:
        model = NGSPanel
        fields = ('NGS_Panel_Name', 'Gene_IDs', 'Transcript_IDs', 'Virtual_Panels')

class NewGeneForm(forms.ModelForm):

    class Meta:
        model = NewGene
        fields = ('Gene_Name', 'Gene_IDs', 'Transcript_IDs', 'Virtual_Panels', 'HUGOgene')

class NewHUGOgeneForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = '__all__'
