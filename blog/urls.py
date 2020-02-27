from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView # Allows us to redirect incorrect urls to the home page

from blog.views.register import RegisterView

urlpatterns = [
    path('home/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:home')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    re_path(r'^.*$', RedirectView.as_view(url='home/', permanent=False), name='index') # Django now uses re-path instead of regex on url. This returns incorrect urls to home.
]