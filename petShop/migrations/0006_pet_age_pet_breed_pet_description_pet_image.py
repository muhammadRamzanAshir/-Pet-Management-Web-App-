# Generated by Django 4.2.16 on 2024-12-20 07:07

from django.db import migrations, models
import petShop.models


class Migration(migrations.Migration):

    dependencies = [
        ('petShop', '0005_customer_pet_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default=petShop.models.get_default_image, upload_to='pets/'),
        ),
    ]
