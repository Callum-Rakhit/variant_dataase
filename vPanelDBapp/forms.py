from django import forms
from .models import NGSPanel, NewSubpanel, HUGOgene

class NGSPanelForm(forms.ModelForm):

    class Meta:
        model = NGSPanel
        fields = ('NGS_Panel_Name', 'Transcript_IDs', 'Virtual_Panels')

class NewSubpanelForm(forms.ModelForm):

    class Meta:
        model = NewSubpanel
        fields = ('Transcript_IDs', 'Virtual_Panels', 'HUGOgene')

class NewHUGOgeneForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = '__all__'
