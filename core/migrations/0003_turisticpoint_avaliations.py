# Generated by Django 2.0.13 on 2021-06-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliations', '0001_initial'),
        ('core', '0002_turisticpoint_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='turisticpoint',
            name='avaliations',
            field=models.ManyToManyField(to='avaliations.Avaliation'),
        ),
    ]