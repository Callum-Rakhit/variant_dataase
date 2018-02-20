from models import Panel, Subpanel


class PanelAutocomplete(autocomplete_light.AutocompleteGenericBase):
    model = Panel
    choices = (
        Panel.objects.all(),
    )
    search_fields = (
        ('^gene', )
    )
    limit_choices = 10
    autocomplete_light.register(SubscriptionAppAutocomplete)


class SubpanelAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = Subpanel
    choices = Subpanel.objects.all()
    search_fields = ('gene', )
    limit_choices = 10
    autocomplete_light.register(SubscriptionAutocomplete)