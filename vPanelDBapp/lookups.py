from ajax_select import register, LookupChannel
from .models import HUGOgene

@register('hugogenes')
class HUGOgeneLookup(LookupChannel):

    model = HUGOgene

    def get_query(self, q, request):
          return self.model.objects.filter(title__icontains=q).order_by('title')