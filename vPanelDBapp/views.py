from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NGSPanel, NewGene, HUGOgene
from .forms import NGSPanelForm, NewGeneForm, NewHUGOgeneForm
from django.views import generic
# from django.contrib.auth.decorators import login_required


def home_page(request):
    title = "Panel Database"
    context = {
        "title": title,
    }
    return render(request, "vPanelDBapp/home.html", context)


def panel_new(request):
    if request.method == "POST":
        form = NGSPanelForm(request.POST)
        if form.is_valid():
            panel = form.save(commit=False)
            panel.author = request.user
            panel.published_date = timezone.now()
            panel.save()
            return redirect('/')
    else:
        form = NGSPanelForm()
        title = "Add a new panel"
    context = {
        "title": title,
        'form': form
    }
    return render(request, 'vPanelDBapp/panel_edit.html', {'form': form})


def panel_edit(request, pk):
    panel = get_object_or_404(NGSPanel, pk=pk)
    if request.method == "POST":
        form = NGSPanelForm(request.POST, instance=panel)
        if form.is_valid():
            panel = form.save(commit=False)
            panel.author = request.user
            panel.published_date = timezone.now()
            panel.save()
            return redirect('panel_detail', pk=panel.pk)
    else:
        form = NGSPanelForm(instance=panel)
    return render(request, 'vPanelDBapp/panel_edit.html', {'form': form})


def panel_detail(request, pk):
    panel = get_object_or_404(NGSPanel, pk=pk)
    return render(request, 'vPanelDBapp/panel_detail.html', {'panel': panel})


def panel_list(request):
    panel = NGSPanel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'vPanelDBapp/panel_list.html', {'panels': panel})


def gene_new(request):
    if request.method == "POST":
        form = NewGeneForm(request.POST)
        title = "New Gene Added"
        if form.is_valid():
            gene = form.save(commit=False)
            gene.author = request.user
            gene.published_date = timezone.now()
            gene.save()
    else:
        form = NewGeneForm()
        title = "Add a new gene"
    context = {
            "title": title,
            'form': form
    }
    return render(request, "vPanelDBapp/gene_edit.html", context)


def gene_edit(request, pk):
    panel = get_object_or_404(NewGene, pk=pk)
    if request.method == "POST":
        form = NewGeneForm(request.POST, instance=panel)
        if form.is_valid():
            gene = form.save(commit=False)
            gene.author = request.user
            gene.published_date = timezone.now()
            gene.save()
            return redirect('gene_detail', pk=gene.pk)
    else:
        form = NewGeneForm(instance=panel)
    return render(request, 'vPanelDBapp/gene_edit.html', {'form': form})


def gene_detail(request, pk):
    gene = get_object_or_404(NewGene, pk=pk)
    return render(request, 'vPanelDBapp/gene_detail.html', {'gene': gene})


def gene_list(request):
    gene = NewGene.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'vPanelDBapp/gene_list.html', {'genes': gene})


def new_hugogene(request):
    if request.method == "POST":
        form = NewHUGOgeneForm(request.POST)
        title = "New HUGO Gene Added"
        if form.is_valid():
            hugogene = form.save(commit=False)
            hugogene.save()
            return redirect('/')
    else:
        form = NewHUGOgeneForm()
        title = "Add a new HUGO Gene"
    context = {
            "title": title,
            'form': form
    }
    return render(request, 'vPanelDBapp/new_hugogene.html', {'form': form})


class HUGOListView(generic.ListView):
    model = HUGOgene
    context_object_name = 'HUGO_gene_list'  # template variable
    template_name = 'books/HUGO_gene_symbol_list.html'  # template name/location


class HUGODetailView(generic.DetailView):
    model = HUGOgene