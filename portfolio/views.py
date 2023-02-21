from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def blogs(request):
    return render(request, "portfolio/blogs.html", {
        "blogs": Blog.objects.all()
    })