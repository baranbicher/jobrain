from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name = "jobs"),
    path('<slug:category_slug>/<slug:job_slug>', views.job_detail, name = "job_details"),
    path('<slug:category_slug>', views.category_list, name = "jobs_by_category"),
    path('<slug:location_slug>', views.category_list, name = "jobs_by_location"),
    path('search/', views.search, name = "search"),
]
