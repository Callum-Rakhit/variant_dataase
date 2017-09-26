from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NGSPanel, NewGene#, Panel
from .forms import NGSPanelForm, NewGeneForm#, NewPanelForm
# from django.contrib.auth.decorators import login_required

def home_page(request):
    title = "Panel Database"
    context = {
        "title": title,
    }
    return render(request, "blog/home.html", context)

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
    return render(request, 'blog/panel_edit.html', {'form': form})

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
    return render(request, 'blog/panel_edit.html', {'form': form})

def panel_detail(request, pk):
    panel = get_object_or_404(NGSPanel, pk=pk)
    return render(request, 'blog/panel_detail.html', {'panel': panel})

def panel_list(request):
    panel = NGSPanel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/panel_list.html', {'panels': panel })

def gene(args):
    pass

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
    return render(request, "blog/gene_new.html", context)

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
    return render(request, 'blog/gene_edit.html', {'form': form})

def gene_detail(request, pk):
    gene = get_object_or_404(NewGene, pk=pk)
    return render(request, 'blog/gene_detail.html', {'gene': gene})

def gene_list(request):
    gene = NewGene.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/gene_list.html', {'genes': gene })