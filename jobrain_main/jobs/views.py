from django.shortcuts import render
from . models import Job, Category
#FOR FILTER

from django_filters.views import FilterView
from .filters import JobFilter

class JobFilterView(FilterView):
    model = Job
    template_name = 'jobs.html'
    paginate_by = 10
    filterset_class = JobFilter

# Create your views here.
def job_list(request):
    jobs = Job.objects.all().order_by('-date')
    categories = Category.objects.all()

    context = {
        'jobs': jobs,
        'categories': categories
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

