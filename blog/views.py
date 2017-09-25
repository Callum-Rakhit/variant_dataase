from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Panel
from .forms import PostForm, NewPanelForm
from django.contrib.auth.decorators import login_required

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_panel(request):
    title = "Add a new Panel"
    if request.method == "POST":
        form = NewPanelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('.', pk=post.pk)
    else:
        form = NewPanelForm()
        title = "Add a new Panel"
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "blog/newform.html", context)

def panel_list(request):
    order_by = request.GET.get('order_by', 'PanelName')
    gene_data = Gene.objects.all()
    panel_info = Panel.objects.all().order_by(order_by)
    context = {
        "panel_detail": panel_info,
        "title": "List of all Panels",
        "gene_data": gene_data,
    }
    return render(request, "panel_list.html", context)

def home_page(request):
    title = "Welcome to the Primer Database"
    context = {
        "title": title,
    }
    return render(request, "blog/home.html", context)

def gene_list(request):
    title = "Welcome to the Primer Database"
    context = {
        "title": title,
    }
    return render(request, "blog/genes.html", context)
