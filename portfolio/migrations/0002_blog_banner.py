# Generated by Django 4.1 on 2023-02-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='banner',
            field=models.URLField(default='/static/portfolio/images/blogs/defaultblog.jpg'),
        ),
    ]