# Generated by Django 4.2.16 on 2024-12-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petShop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='title',
        ),
    ]
