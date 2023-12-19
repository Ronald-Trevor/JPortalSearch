from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect
from . models import Job
from django.contrib import messages


# Create your views here.
def jobs(request):
    # fetch the posted jobs
    jobs = Job.objects.all()
    return render (request, 'Jobs.html', {
        'jobs':jobs
    })

def home(request):
    return render (request, 'Home.html')

def addjob(request):
    if request.method == 'POST':
        # extract the data from the request body
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        company = request.POST['company']
        email = request.POST['email']
        contact = request.POST['contact']
        location = request.POST['location']
        qualifications = request.POST['qualifications']
        skills = request.POST['skills']

        # Perform basic form validations and ensure the form is not empty
        if not title or not description or not category or not company or not email or not contact or not location or not qualifications or not skills:
            messages.error(request, 'Please fill in all the required fields.')
        # Check if the phone contact is valid
        elif len(contact) < 10:
            messages.error(request, 'Contact number must be at least 10 characters.')

        else:
            # create a new job object
            job = Job.objects.create(title=title, description=description, category=category, 
                                    company=company, email=email, contact=contact, 
                                    location=location,qualifications=qualifications, skills=skills)
                                    
            # save the new Job object in the database
            job.save()
            return redirect(request.build_absolute_uri('/jobs'))

    return render (request, 'AddJobForm.html')


# fetch job deatails for a specific job
def jobdetails(request,id):
    jobdetails = Job.objects.get(id=id)
    return render (request, 'JobDetails.html',{
        'jobdetails':jobdetails
    })



