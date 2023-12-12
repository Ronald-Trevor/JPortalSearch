from django.db import models

# Create your models here.

class Job(models.Model):

    # Defining the allowed values for the job type to ensure users only enter correct data
    class JobTypeOptions(models.TextChoices):
        FULLTIME = "FT", ("Full Time")
        PARTTIME = "PT", ("Part Time")
        
    title = models.CharField(max_length= 20)
    description = models.TextField()
    category = models.CharField(max_length=10)
    company = models.CharField(max_length= 20)
    location = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=10, default="FT" , choices=JobTypeOptions.choices)
    qualifications = models.TextField()
    skills = models.TextField()
    email = models.EmailField()
    contact = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.title


