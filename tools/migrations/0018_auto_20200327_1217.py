# Generated by Django 3.0.4 on 2020-03-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0017_auto_20200327_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('-modified_date',)},
        ),
        migrations.AlterField(
            model_name='inspiration',
            name='name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='learning',
            name='name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
