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
        fields = ('subpanelName', 'subpanelID', 'username', 'subpanelVersion', 'panel', 'gene')

    def __init__(self, *args, **kwargs):

        parent_panel = kwargs.pop('parent_panel')
        print(parent_panel)
        super(SubpanelForm, self).__init__(*args, **kwargs)

        # query if gene in parent_panel (Panel)
        # Panel.pk
        self.fields['gene'].queryset = HUGOgene.objects.filter(pk=parent_panel)

