from django.db import models

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    
    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=70, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=70, unique=True)
    
    
    def __str__(self):
        return self.name
    
class JobType(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=300, unique=True, verbose_name="Job Name", help_text="Job name write")
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(blank=True, null=True, )
    image = models.ImageField(upload_to="jobs/%Y/%m/%d/", default="jobs/jobs-default-image.png")
    date = models.DateField(auto_now=False)
    available = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    jobtype = models.ForeignKey(JobType, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Job Type")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.DO_NOTHING, blank=True, null=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, blank=True, null=True)
    vacancy = models.CharField(max_length=15, null=True)
    tags = models.ManyToManyField(Tag, max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    