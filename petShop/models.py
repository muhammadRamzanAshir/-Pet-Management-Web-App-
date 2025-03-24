from django.db import models
import os
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Hero(models.Model):
    image        = models.ImageField(upload_to='hero/')
    tagline      = models.CharField(max_length=255)
    Pet_listing  = models.URLField(default='http://example.com')

    def __str__(self):
        return self.tagline

class Service(models.Model):
    ICON_CHOICES = [
        ('flaticon-blind', 'Dog Walking Icon'),
        ('flaticon-dog-eating', 'Pet Daycare Icon'),
        ('flaticon-grooming', 'Pet Grooming Icon'),
        # Add more icons as needed
    ]

    title = models.CharField(max_length=255)  # For the <h3> heading
    description = models.TextField()  # For the <p> content
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)  # For the icon class
    link = models.URLField()  # For the "Read more" link

    def __str__(self):
        return self.title

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255, default="Why Choose Us?")
    background_image = models.ImageField(upload_to="images/")  # For the background image

    def __str__(self):
        return self.title

class WhyChooseUsItem(models.Model):
    ICON_CHOICES = [
        ('flaticon-stethoscope', 'Stethoscope Icon'),
        ('flaticon-customer-service', 'Customer Service Icon'),
        ('flaticon-emergency-call', 'Emergency Call Icon'),
        ('flaticon-veterinarian', 'Veterinarian Icon'),
        # Add more icons as needed
    ]

    section = models.ForeignKey(WhyChooseUs, on_delete=models.CASCADE, related_name='items')
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)  # Icon class
    heading = models.CharField(max_length=255)  # Service heading
    description = models.TextField()  # Service description

    def __str__(self):
        return self.heading

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)


def get_default_image():
    return os.path.join('pets', 'default_image.jpg')

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pets/')
    date_added = models.DateTimeField(default=datetime.datetime.now)  # Set a default manually

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Answer(models.Model):
    faq = models.ForeignKey(FAQ, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer

class Veteran(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff_photos/')
    description = models.TextField()
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    google_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class PetAdoption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adopted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} adopted {self.pet.name}"