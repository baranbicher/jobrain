from django.shortcuts import render
from . models import Job, Category, Location, JobType, Experience, Qualification, Gender
#FOR FILTER

# from django_filters.views import FilterView
from .filters import JobFilter

#search multi required
from django.db.models import Q

# paganition system
from django.core.paginator import Paginator, EmptyPage

from django.utils.html import mark_safe
from django.utils.html import escape
import re

def highlight_search_term(text, search_term):
    # Öncelikle metin ve arama terimi HTML injection'a karşı escape edilir.
    text = escape(text)
    search_term = escape(search_term)
    
    # Arama terimini vurgulamak için HTML mark-up kullanılacak.
    highlighted = re.sub(
        f"({search_term})", 
        r"<mark>\1</mark>", 
        text, 
        flags=re.IGNORECASE
    )
    
    # Güvenli bir string olarak işaretleyip geri dönülür.
    return mark_safe(highlighted)
# Create your views here.
def job_list(request):
    jobs = Job.objects.all().order_by('-date')
    locations = Location.objects.all()
    categories = Category.objects.all()
    jobtypes = JobType.objects.all()
    experiences = Experience.objects.all()
    qualifications = Qualification.objects.all()
    genders = Gender.objects.all()

    # Arama sorgusu
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    #filter start
    my_filter = JobFilter(request.GET, queryset=jobs)
    jobs = my_filter.qs
    #filter done
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', 1)
    try:
        jobs = paginator.page(page_number)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    highlighted_jobs = []
    for job in jobs:
        job.name = highlight_search_term(job.name, search_query)
        job.description = highlight_search_term(job.description, search_query)
        job.category.name = highlight_search_term(job.category.name, search_query)
        highlighted_jobs.append(job)

    context = {
        'jobs': highlighted_jobs,
        'categories': categories,
        'locations': locations,
        'jobtypes': jobtypes,
        'experiences': experiences,
        'qualifications': qualifications,
        'genders': genders,
        'my_filter': my_filter,
        'search_query': search_query,
    }
    

    return render(request, 'jobs.html', context)

def job_detail(request, category_slug, job_slug):
    job = Job.objects.get(category__slug=category_slug, slug = job_slug)

    context = {
        'job': job
    }

    return render(request, 'job_details.html', context)

def category_list(request, category_slug):
    jobs = Job.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()

    context = {
        'jobs': jobs,
        'categories': categories
    }

    return render(request, 'jobs.html', context)

def location_list(request, location_slug):
    jobs = Job.objects.all().filter(location__slug=location_slug)
    locations = Location.objects.all()

    context = {
        'jobs': jobs,
        'locations': locations
    }

    return render(request, 'jobs.html', context)


