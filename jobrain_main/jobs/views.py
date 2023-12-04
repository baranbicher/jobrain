from django.shortcuts import render
from . models import Job, Category, Location, JobType, Experience, Qualification, Gender
#FOR FILTER

# from django_filters.views import FilterView
from .filters import JobFilter


# Create your views here.
def job_list(request):
    jobs = Job.objects.all().order_by('-date')
    locations = Location.objects.all()
    categories = Category.objects.all()
    jobtypes = JobType.objects.all()
    experiences = Experience.objects.all()
    qualifications = Qualification.objects.all()
    genders = Gender.objects.all()

    #filter start
    my_filter = JobFilter(request.GET, queryset=jobs)
    jobs = my_filter.qs
    #filter done

    context = {
        'jobs': jobs,
        'categories': categories,
        'locations': locations,
        'jobtypes': jobtypes,
        'experiences': experiences,
        'qualifications': qualifications,
        'genders': genders,
        'my_filter': my_filter,
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

