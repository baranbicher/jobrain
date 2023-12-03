import django_filters

from . models import Job

class JobFilter(django_filters.FilterSet):

    class Meta:
        model = Job
        fields = ['location', 'category', 'experience', 'qualification', 'jobtype', 'gender']