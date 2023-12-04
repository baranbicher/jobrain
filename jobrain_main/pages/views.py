from django.shortcuts import render
from django.views.generic import TemplateView
from jobs.models import Job, Category, Location

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(available=True).order_by('-date')[:5]
        context['total_job'] = Job.objects.filter(available=True).count()
        context['categories'] = Category.objects.all().order_by()[:8]
        context['locations'] = Location.objects.all()
        return context