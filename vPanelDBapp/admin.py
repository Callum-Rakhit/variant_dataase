from django.contrib import admin
from .models import HUGOgene, Panel, Subpanel
from ajax_select import make_ajax_form
from ajax_select.fields import autoselect_fields_check_can_add

admin.site.register(HUGOgene)
admin.site.register(Panel)
admin.site.register(Subpanel)

'''

class AjaxSelectAdmin(admin.ModelAdmin):
    """ in order to get + popup functions subclass this or do the same hook inside of your get_form """

    def get_form(self, request, obj=None, **kwargs):
        form = super(AjaxSelectAdmin, self).get_form(request, obj, **kwargs)

        autoselect_fields_check_can_add(form, self.model, request.user)
        return form


@admin.register(HUGOgene)
class HUGOgeneLookupFormAdmin(AjaxSelectAdmin):

    form = make_ajax_form(HUGOgene, {
        'symbol': 'symbol'
    })

'''