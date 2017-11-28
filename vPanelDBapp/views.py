import re  # Needed for search function
from django.db.models import Q  # Needed for search function
from .models import Panel, Subpanel, HUGOgene
from django.contrib.auth.decorators import login_required
from .forms import PanelForm, SubpanelForm, HUGOgeneLookupForm
from django.shortcuts import render, get_object_or_404, redirect

from dal import autocomplete


class PanelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Panel.objects.none()

        qs = Panel.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


def home_page(request):
    title = "Panel Database"
    context = {
        "title": title,
    }
    return render(request, "vPanelDBapp/home.html", context)


@login_required
def panel_new(request):
    if request.method == "POST":
        form = PanelForm(request.POST)
        if form.is_valid():
            panel = form.save(commit=False)
            panel.save()
            return redirect('/')
    else:
        form = PanelForm()
        title = "Add a new panel"
    context = {
        "title": title,
        'form': form
    }
    return render(request, 'vPanelDBapp/panel_edit.html', {'form': form})


@login_required
def panel_edit(request, pk):
    panel = get_object_or_404(Panel, pk=pk)
    if request.method == "POST":
        form = PanelForm(request.POST, instance=panel)
        if form.is_valid():
            panel = form.save() # (commit=False) allows you to commit to the form without saving but breaks m2m saving
            panel.save()
            return redirect('panel_detail', pk=panel.pk)
    else:
        form = PanelForm(instance=panel)
    return render(request, 'vPanelDBapp/panel_edit.html', {'form': form})


def panel_detail(request, pk):
    panel = get_object_or_404(Panel, pk=pk)
    return render(request, 'vPanelDBapp/panel_detail.html', {'panel': panel})


def panel_list(request):
    panel = Panel.objects.all()
    return render(request, 'vPanelDBapp/panel_list.html', {'panels': panel})


@login_required
def subpanel_new(request):

    if request.method == "POST" and 'update' in request.POST:

        parent_panel = request.POST['panel']
        form = SubpanelForm(request.POST, parent_panel=parent_panel)

    elif request.method == "POST":
        parent_panel = request.POST['panel']
        form = SubpanelForm(request.POST, parent_panel=parent_panel)

        if form.is_valid():
            subpanel = form.save()  # (commit=False) allows you to commit to the form without saving but breaks m2m saving
            subpanel.save()
            return redirect('/')

    else:
        form = SubpanelForm(parent_panel=None)

    title = "Add a new Subpanel"
    context = {
            "title": title,
            'form': form
    }
    return render(request, "vPanelDBapp/subpanel_edit.html", context)

@login_required
def subpanel_edit(request, pk):
    subpanel = get_object_or_404(Subpanel, pk=pk)

    if request.method == "POST" and 'update' in request.POST:

        parent_panel = request.POST['panel']
        form = SubpanelForm(request.POST, parent_panel=parent_panel)

    elif request.method == "POST":

        parent_panel = request.POST['panel']
        form = SubpanelForm(request.POST, parent_panel=parent_panel)

        if form.is_valid():
            subpanel = form.save()
            subpanel.save()
            return redirect('subpanel_detail', pk=subpanel.pk)

    else:
        form = SubpanelForm(parent_panel=None)
    return render(request, 'vPanelDBapp/subpanel_edit.html', {'form': form})


def subpanel_detail(request, pk):
    subpanel = get_object_or_404(Subpanel, pk=pk)
    return render(request, 'vPanelDBapp/subpanel_detail.html', {'subpanel': subpanel})


def subpanel_list(request):
    subpanel = Subpanel.objects.all()
    return render(request, 'vPanelDBapp/subpanel_list.html', {'subpanels': subpanel})


@login_required
def hugogene_new(request):
    if request.method == "POST":
        form = HUGOgeneLookupForm(request.POST)
        title = "New HUGO Gene Added"
        if form.is_valid():
            hugogene = form.save(commit=False)
            hugogene.save()
            return redirect('/')
    else:
        form = HUGOgeneLookupForm()
        title = "Add a new HUGO Gene"
    context = {
            "title": title,
            'form': form
    }
    return render(request, 'vPanelDBapp/hugogene_edit.html', {'form': form})


@login_required
def hugogene_edit(request, pk):
    hugogene = get_object_or_404(HUGOgene, pk=pk)

    if request.method == "POST":
        form = HUGOgeneLookupForm(request.POST, instance=hugogene)
        if form.is_valid():
            hugogene = form.save(commit=False)
            hugogene.save()
            return redirect('hugogene_edit', pk=hugogene.pk)
    else:
        form = HUGOgeneLookupForm(instance=hugogene)
    return render(request, 'vPanelDBapp/hugopanel_edit.html', {'form': form})


def hugogene_detail(request, pk):
    hugogene = get_object_or_404(HUGOgene, pk=pk)
    return render(request, 'vPanelDBapp/hugogene_detail.html', {'hugogene': hugogene})


def hugogene_list(request):
    hugogene = HUGOgene.objects.all()
    return render(request, 'vPanelDBapp/hugogene_list.html', {'hugogenes': hugogene})

# https://www.julienphalip.com/blog/adding-search-to-a-django-site-in-a-snap/

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


''' 

Splits the query string in individual keywords, to remove unnecessary spaces
and group quoted words together.

Example:

>>> normalize_query('  some random  words "with   quotes  " and   spaces')
['some', 'random', 'words', 'with quotes', 'and', 'spaces']

'''


def get_query(query_string, search_fields):
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


'''

Returns a query that is a combination of Q objects. That combination
aims to search keywords within a model by testing the given search fields.

'''


def search(request):  # Search view
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        hugogene_query =  get_query(query_string, ['symbol', 'ensemblGeneID',
                                                   'locationSortable'])
        hugogene_entries = HUGOgene.objects.filter(hugogene_query)
        title = "Search Results"
        context = {
            'query_string': query_string,
            'hugogene_entries': hugogene_entries,
            'title': title,
        }
    return render(request, "vPanelDBapp/search_results.html", context)