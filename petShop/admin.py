from django.contrib import admin
from .models import Hero, Service, WhyChooseUsItem, WhyChooseUs, Pet, FAQ, Answer, Veteran, PetAdoption

# Register your models here.

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('tagline',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'link')

class WhyChooseUsItemInline(admin.TabularInline):
    model = WhyChooseUsItem
    extra = 1  # Number of extra empty rows in the admin panel

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    inlines = [WhyChooseUsItemInline]
    list_display = ('title',)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed')

# PetAdoption registration
@admin.register(PetAdoption)
class PetAdoptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'adopted_at')

admin.site.register(FAQ)
admin.site.register(Answer)

@admin.register(Veteran)
class VeteranAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name',)
