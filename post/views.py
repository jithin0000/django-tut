from django.shortcuts import render

# Create your views here.

def home(request):
    """ post index view """

    return render(request, "post/home.html", { 'title' : 'Django tutorial' })


def details(request, pk):
    """ detail view of post """

    return render(request, "post/detail.html", { 'id' : pk })


def addPost(request):
    """ view for creating post """
    return render(request, 'post/add_post.html', {  })

def updatePost(request, pk):
    """ view for updating post """
    return render(request, 'post/update_post.html', { "id" : pk })

def deletePost(request, pk):
    """ view for delete post """
    return render(request, 'post/delete_post.html', { "id" : pk })

















