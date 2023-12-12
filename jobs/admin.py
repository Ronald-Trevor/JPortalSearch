from django.contrib import admin
from . models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ("title","category","company","location")

admin.site.register(Job, JobAdmin)

