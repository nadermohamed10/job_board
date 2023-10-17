
from django.urls import path 

from . import views

app_name = 'job'
urlpatterns = [
   
    path('', views.job_list),
    path('<str:slug>', views.job_details , name='one_job')
]
