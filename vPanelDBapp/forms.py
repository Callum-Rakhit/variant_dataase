from django import forms
from .models import NGSPanel, NewGene, Test

class NGSPanelForm(forms.ModelForm):

    class Meta:
        model = NGSPanel
        fields = ('NGS_Panel_Name', 'Gene_IDs', 'Transcript_IDs', 'Virtual_Panels')

class NewGeneForm(forms.ModelForm):

    class Meta:
        model = NewGene
        fields = ('Gene_Name', 'Gene_IDs', 'Transcript_IDs', 'Virtual_Panels', 'Test')

class NewTestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = '__all__'
