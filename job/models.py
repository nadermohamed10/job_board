from typing import Any
from django.db import models
from django.utils.text import slugify

# Create your models here.

'''
django models field :

    for
        -html widget
        -validation
        -db size
'''

JOB_TYPE = [

    ('full time' , 'full time'),
    ('part time' , 'part time')
]


class job (models.Model) : #table

    title = models.CharField(max_length=100) #field
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE) #field
    description = models.TextField(max_length=1000) #field 
    publshed_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs')

    slug = models.SlugField(blank=True , null=True)

    def save(self , *args , **kwargs) :
        self.slug = slugify(self.title)
        super(job, self).save(*args , **kwargs)


    def __str__(self) :
        return self.title
    

class category (models.Model) :
    name = models.CharField(max_length=25)

    def __str__(self) :
        return self.name