from django.contrib import admin
from . models import Job, Location, JobType, Category, Experience, Qualification, Gender, Tag

# Register your models here.

# admin.site.register(Job)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields= ('name', 'description')
    prepopulated_fields={'slug':('name',)}

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

# admin.site.register(Location)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(JobType)

admin.site.register(Experience)

admin.site.register(Qualification)

admin.site.register(Gender)
