# Generated by Django 3.0.4 on 2020-04-05 17:03

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0023_auto_20200403_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('name', models.CharField(max_length=100)),
                ('preamble', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('image_url', models.URLField(blank=True, default='', max_length=250, null=True)),
                ('youtube', models.URLField(blank=True, default='', max_length=250, null=True)),
                ('text', tinymce.models.HTMLField(blank=True, default='', null=True)),
                ('image', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
