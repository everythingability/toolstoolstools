# Generated by Django 3.0.4 on 2020-03-26 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_auto_20200326_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='slug',
        ),
    ]
