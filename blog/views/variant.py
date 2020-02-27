from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from blog.models.variant_and_metadata import Variant


class VariantView(generic.DetailView):
    model = Variant
    template_name = 'variant/variant.html'


class VariantCreate(LoginRequiredMixin, CreateView):
    model = Variant
    fields = ['name', 'age', 'proband_affected', 'relatives', 'stage', 'description', 'sequencer',
    'variant_cDNA', 'variant_protein', 'variant_genome', 'pathogenicity_code', 'evidence']
    template_name = 'variant/create_variant.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VariantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Variant
    fields = ['name', 'age', 'proband_affected', 'relatives', 'stage', 'description', 'sequencer',
    'variant_cDNA', 'variant_protein', 'variant_genome', 'pathogenicity_code', 'evidence']
    template_name = 'variant/create_variant.html'
    login_url = reverse_lazy('login')

    def test_func(self):
        return Variant.objects.get(id=self.kwargs['pk']).user == self.request.user


class VariantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Variant
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('login')

    def test_func(self):
        return Variant.objects.get(id=self.kwargs['pk']).user == self.request.user
        