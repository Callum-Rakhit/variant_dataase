from django import forms
from .models import Panel, Subpanel, HUGOgene
from ajax_select.fields import AutoCompleteSelectMultipleField


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = ('gene',)

    tags = AutoCompleteSelectMultipleField('tags')


class HUGOgeneLookupForm(forms.ModelForm):

    class Meta:
        model = HUGOgene
        fields = ('symbol', 'locationSortable', 'ensemblGeneID')


class PanelForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = ('panelName', 'panelID', 'username', 'panelVersion', 'gene')
        labels = {  # Add custom names to modelform labels
            'panelName': 'Panel Name',
            'panelID': 'Panel ID',
            'username': 'Username',
            'panelVersion': 'Panel Version'
        }


class SubpanelForm(forms.ModelForm):

    class Meta:
        model = Subpanel
        fields = ('subpanelName', 'subpanelID', 'username', 'subpanelVersion', 'panel', 'gene')
        labels = {  # Add custom names to modelform labels
            'subpanelName': 'Subpanel Name',
            'subpanelID': 'Subpanel ID',
            'username': 'Username',
            'subpanelVersion': 'Subpanel Version'
        }

    def __init__(self, *args, **kwargs):

        parent_panel = kwargs.pop('parent_panel')
        print(type(parent_panel))
        super(SubpanelForm, self).__init__(*args, **kwargs)
        # query if gene in parent_panel (Panel)
        if parent_panel:
            self.fields['gene'].queryset = HUGOgene.objects.filter(panel__id=int(parent_panel))
        else:
            pass