from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout , Field, Fieldset
from .models import Post, Panel

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Panel_Name', 'genes', 'subpanels')

class NewPanelForm(forms.ModelForm):
    Notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        label='Notes',
        required=False,
    )

    class Meta:
        model = Panel
        fields = ['PanelName', 'Notes']

    def __init__(self, *args, **kwargs):
        super(NewPanelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))
