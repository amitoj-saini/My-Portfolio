from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('blogs',  views.blogs, name="blogs")
]