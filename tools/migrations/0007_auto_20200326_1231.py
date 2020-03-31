# Generated by Django 3.0.4 on 2020-03-26 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_level_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('url', models.URLField(default='', max_length=250, null=True)),
                ('image_url', models.URLField(blank=True, default='', max_length=250, null=True)),
                ('about', models.TextField(blank=True, default='', null=True)),
                ('altcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='icategory2', to='tools.Category')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='icategory1', to='tools.Category')),
                ('tags', models.ManyToManyField(to='tools.Tag')),
            ],
        ),
    ]
