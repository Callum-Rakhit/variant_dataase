from django import forms
from .models import Panel, Subpanel, HUGOgene

class PanelForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = ('Panel_Name', 'Panel_ID', 'Username', 'Panel_Version','HUGOgene')

class SubpanelForm(forms.ModelForm):

    class Meta:
        model = Subpanel
        fields = ('Subpanel_Name', 'Subpanel_ID', 'Username', 'Subpanel_Version','HUGOgene', 'Panel')

class HUGOgeneForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = ('HUGO_Gene_ID',)