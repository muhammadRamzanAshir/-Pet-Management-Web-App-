from django.shortcuts import redirect, render
from .models import Hero,Service,WhyChooseUs
from .models import Customer, Product, Pet,FAQ,Veteran,PetAdoption
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    hero_slides = Hero.objects.all()
    services = Service.objects.all()
    section = WhyChooseUs.objects.prefetch_related('items').first()
    pets = Pet.objects.all()
    latest_pets = Pet.objects.all().order_by('-date_added')[:5]
    faqs = FAQ.objects.all()

    # Get the total count of adopted pets
    total_adopted_pets = PetAdoption.objects.count()

    # Get the total count of users
    total_users = User.objects.count()

    # Get the total count of products
    total_products = Product.objects.count()

    # Add the adoption status for each pet
    for pet in pets:
        # Check if the pet is adopted
        pet.is_adopted = PetAdoption.objects.filter(pet=pet).exists()

    context = {
        'hero_slides': hero_slides,
        'services': services,
        'section': section,
        'total_users': total_users,  # Total users count
        'total_products': total_products,  # Total products count
        'total_pets': Pet.objects.count(),
        'total_adopted_pets': total_adopted_pets,
        'pets': pets,
        'latest_pets': latest_pets,
        'faqs': faqs,
    }

    return render(request, 'index.html', context)


def about(request):
    section = WhyChooseUs.objects.prefetch_related('items').first()
    latest_pets = Pet.objects.all().order_by('-date_added')[:5]
    faqs = FAQ.objects.all()
    
    context = {
        'section':section,
        'total_customers': Customer.objects.count(),
        'total_products': Product.objects.count(),
        'total_pets': Pet.objects.count(),
        'latest_pets':latest_pets,
        'faqs':faqs,
    }
    return render(request, 'about.html', context)


def vet(request):
    latest_pets = Pet.objects.all().order_by('-date_added')[:5]
    veterans = Veteran.objects.all()
    return render(request, 'vet.html', {'veterans': veterans,
                                        'latest_pets': latest_pets})

def services(request):
    section = WhyChooseUs.objects.prefetch_related('items').first()
    services = Service.objects.all()
    return render(request, 'service.html',{'services': services, "section":section,})

def gallery(request):
    pets = Pet.objects.all()
    return render(request, 'gallery.html', {'pets':pets})

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the home page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the home page after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index') 

@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    # Save the adoption to the database
    adoption = PetAdoption.objects.create(user=request.user, pet=pet)

    # Add a success message
    messages.success(request, f"Congratulations! You have successfully adopted {pet.name}.")

    # Redirect to the index page
    return redirect('index')  # Redirect to the index page after adoption