# Generated by Django 3.0.4 on 2020-03-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0015_activity_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='learnings',
            field=models.ManyToManyField(blank=True, null=True, to='tools.Learning'),
        ),
    ]
