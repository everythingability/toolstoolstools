# Generated by Django 3.0.4 on 2020-03-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='about',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]
