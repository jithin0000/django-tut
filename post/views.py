from django.shortcuts import render

# Create your views here.

def index(request):
    """ post index view """

    return render(request, "post/home.html", {})
