from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout , Field, Fieldset
from .models import NGSPanel#, Panel


class NGSPanelForm(forms.ModelForm):

    class Meta:
        model = NGSPanel
        fields = ('NGS_Panel_Name', 'Gene_IDs', 'Transcript_IDs', 'Virtual_Panels')