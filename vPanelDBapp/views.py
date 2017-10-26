from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NGSPanel, NewSubpanel, HUGOgene
from .forms import NGSPanelForm, NewSubpanelForm, NewHUGOgeneForm
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
            panel.save()
            return redirect('panel_detail', pk=panel.pk)
    else:
        form = NGSPanelForm(instance=panel)
    return render(request, 'vPanelDBapp/panel_edit.html', {'form': form})


def panel_detail(request, pk):
    panel = get_object_or_404(NGSPanel, pk=pk)
    return render(request, 'vPanelDBapp/panel_detail.html', {'panel': panel})


def panel_list(request):
    panel = NGSPanel.objects.all()
    return render(request, 'vPanelDBapp/panel_list.html', {'panels': panel})


def subpanel_new(request):
    if request.method == "POST":
        form = NewSubpanelForm(request.POST)
        title = "New Subpanel Added"
        if form.is_valid():
            subpanel = form.save(commit=False)
            subpanel.author = request.user
            subpanel.save()
    else:
        form = NewSubpanelForm()
        title = "Add a new Subpanel"
    context = {
            "title": title,
            'form': form
    }
    return render(request, "vPanelDBapp/subpanel_edit.html", context)


def subpanel_edit(request, pk):
    panel = get_object_or_404(NewSubpanel, pk=pk)
    if request.method == "POST":
        form = NewSubpanelForm(request.POST, instance=panel)
        if form.is_valid():
            subpanel = form.save(commit=False)
            subpanel.author = request.user
            subpanel.save()
            return redirect('subpanel_detail', pk=subpanel.pk)
    else:
        form = NewSubpanelForm(instance=panel)
    return render(request, 'vPanelDBapp/subpanel_edit.html', {'form': form})


def subpanel_detail(request, pk):
    subpanel = get_object_or_404(NewSubpanel, pk=pk)
    return render(request, 'vPanelDBapp/subpanel_detail.html', {'subpanel': subpanel})


def subpanel_list(request):
    subpanel = NewSubpanel.objects
    return render(request, 'vPanelDBapp/subpanel_list.html', {'subpanels': subpanel})


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