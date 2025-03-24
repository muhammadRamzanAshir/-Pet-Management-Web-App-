from django.urls import path
from django.conf.urls.static import static
from pet import settings
from . import views  # Adjust based on your project structure
from .views import logout_view


urlpatterns = [
    path('', views.index, name='index'),  # Example route
    path('about/', views.about, name='about'),  # Example route
    path('vet/', views.vet, name='vet'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
