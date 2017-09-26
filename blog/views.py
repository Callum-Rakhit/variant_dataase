from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NGSPanel#, Panel
from .forms import NGSPanelForm#, NewPanelForm
# from django.contrib.auth.decorators import login_required

def panel_list(request):
    panel = NGSPanel.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/panel_list.html', {'panels': panel })

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

def home_page(request):
    title = "Welcome to the Panel Database"
    context = {
        "title": title,
    }
    return render(request, "blog/home.html", context)


def gene_list(request):
    title = "Genes"
    context = {
        "title": title,
    }
    return render(request, "blog/genes.html", context)