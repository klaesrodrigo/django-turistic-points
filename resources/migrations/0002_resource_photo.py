# Generated by Django 2.0.13 on 2021-06-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='resources'),
        ),
    ]