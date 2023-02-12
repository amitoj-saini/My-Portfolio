from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def blogs(request):
    return render(request, "portfolio/blogs.html")