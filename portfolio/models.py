from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    md = models.URLField(default="")
    banner = models.URLField(default="")
    time = models.DateTimeField(auto_now_add=True)