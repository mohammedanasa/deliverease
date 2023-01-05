from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.conf import settings
from core.models import *



# Create your views here.

@login_required(login_url="/sign-in/?next=/courier/")
def home(request):
    return redirect(reverse('courier:available-jobs'))

    

@login_required(login_url="/sign-in/?next=/courier/")
def available_jobs_page(request):
    return render(request,'courier/available-jobs.html',{
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY
    })

@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page(request, id):
    job = Job.objects.filter(id=id, status=Job.PROCESSING_STATUS).last()
    if not job:
        return redirect(reverse('courier:available-jobs'))

    if request.method == 'POST':
        job.courier = request.user.courier
        job.status = Job.PICKING_STATUS
        job.save()

        return redirect(reverse('courier:available-jobs'))

    
    return render(request,'courier/available-job.html',{
        "job":job
    })

@login_required(login_url="/sign-in/?next=/courier/")
def current_job_page(request):
    job = Job.objects.filter(
        courier=request.user.courier,
        status__in = [
            Job.PICKING_STATUS,
            Job.DELIVERING_STATUS
        ]
        ).last()

    return render(request, 'courier/current-job.html',{
        "job":job,
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY
    })


@login_required(login_url="/sign-in/?next=/courier/")
def current_job_take_photo_page(request, id):
    job = Job.objects.filter(
        id= id,
        courier = request.user.courier,
        status__in = [
            Job.PICKING_STATUS,
            Job.DELIVERING_STATUS
        ]
    ).last()

    if not job: 
        return redirect(reverse('courier:current-job'))
    
    return render(request, 'courier/current-job-take-photo.html',{
        "job": job
    })

@login_required(login_url="/sign-in/?next=/courier/")
def job_complete_page(request):
    return render(request,('courier/job-complete.html'))

@login_required(login_url="/sign-in/?next=/courier/")
def archived_jobs_page(request):
    jobs = Job.objects.filter(
        courier=request.user.courier,
        status=Job.COMPLETED_STATUS
    )
    context = {"anas": 'anas'}
    print(context)
    return render(request,'courier/archived-jobs.html', {'jobs': jobs })

@login_required(login_url="/sign-in/?next=/courier/")
def profile_page(request):
    jobs = Job.objects.filter(
        courier=request.user.courier,
        status= Job.COMPLETED_STATUS
    )
    total_earnings = round(sum(job.price for job in jobs) * 0.8,2)
    total_jobs =len(jobs)
    total_km = sum(job.distance for job in jobs)
    return render(request, 'courier/profile.html', {
        'total_jobs': total_jobs,
        'total_earnings': total_earnings,
        'total_km': total_km
        })