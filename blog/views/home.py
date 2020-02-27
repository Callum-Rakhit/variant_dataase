from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.exceptions import ValidationError

from blog.models.post import Post

NUM_OF_POSTS = 5

def csv_content_validator(csv_file):
    csv_file_content = csv_file.read()
    validation_error_messages = []
    # ...
    # Validate contents of each line
    # Add specific messages to a list variable called
    # `validation_error_messages` for anything that isn't correct.
    # ...
    if validation_error_messages:
        raise ValidationError(" ".join(validation_error_messages))

def home(request, username=None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    if request.method == 'GET':
        post_list = post_list.order_by('-pub_date')

        paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
        page = request.GET.get('page')

        posts = paginator.get_page(page)

        return render(request, 'blog/home.html', {'posts': posts,
                                                  'first_name': first_name,
                                                  'last_name': last_name})
    elif request.method == 'POST':
        pass
        # Easy to check single-variants: https://javatpoint.com/django-file-upload
        # For the bulk uploads, needs to: open the file, and validate every line as if it were a separate entry?