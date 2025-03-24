# Generated by Django 4.2.16 on 2024-12-20 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petShop', '0006_pet_age_pet_breed_pet_description_pet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='pets/'),
        ),
    ]
