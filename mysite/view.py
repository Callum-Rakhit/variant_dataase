from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf

# Authentication views


def login(request):
    c = {
        csrf(request),
    }
    return render_to_response('login.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('logged_out.html')