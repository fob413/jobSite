from django.shortcuts import render
from .models import JobListing

# Create your views here.


def home(request):
    job_listings = JobListing.objects.all()
    context = {'job_listings': job_listings}

    return render(request, "jobs_app/index.html", context)
