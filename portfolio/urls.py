from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('aboutacs',  views.about_acs, name="aboutacs"),
    path('blogs',  views.blogs, name="blogs")
]