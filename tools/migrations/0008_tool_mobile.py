# Generated by Django 3.0.4 on 2020-03-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_auto_20200326_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='mobile',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]