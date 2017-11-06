from django import forms
from .models import Panel, Subpanel, HUGOgene
from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField

class HUGOgeneLookupForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = ('symbol', 'locationSortable', 'ensemblGeneID')
        #tags = AutoCompleteSelectMultipleField('hugogenes', required=False, help_text=None)
        #category = AutoCompleteSelectField('categories', required=False, help_text=None)

class PanelForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = ('panelName', 'panelID', 'username', 'panelVersion','gene')

class SubpanelForm(forms.ModelForm):

    class Meta:
        model = Subpanel
        fields = ('subpanelName', 'subpanelID', 'subpanelVersion', 'username', 'panel', 'gene')


