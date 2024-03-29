from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
)


def image_upload(instance , filename):
    imagename , extension = filename.split(".")
    return "jobs/"


class Job(models.Model):                              #table
    title = models.CharField(max_length=100)          #column
    #location
    job_type = models.CharField(max_length= 15, choices = JOB_TYPE)
    description = models.TextField(max_length =1000 )
    published_at = models.DateTimeField(auto_now= True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    Experience = models.IntegerField(default = 1)
    image = models.ImageField(upload_to="media/")
    slug = models.SlugField(null=True , blank= True)
    
    
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)        
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length= 25)

    def __str__(self):
        return self.name
    
    
class Apply(models.Model):
    appliedjob = models.ForeignKey(Job, on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50)
    cv = models.FileField(upload_to='media/cv/', max_length=100 ,null=True , blank=True)
    coverletter = models.TextField(max_length=500)    
    
    def __str__(self):
        return self.name
    