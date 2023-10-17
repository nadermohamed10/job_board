from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from .models import job

def job_list (request):
    job_list = job.objects.all() #return all jobs in database
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj} #to appere the jobs in front-end templetes and it is name in template is (jobs)
    return render(request , 'job\job_list.html' , context)

def job_details(request , slug):
    job_details = job.objects.get(slug = slug)
    context = {'job' : job_details}
    return render(request , 'job\job_details.html' , context)
