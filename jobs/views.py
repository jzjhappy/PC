from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def Jobs(request):
    return render(request, "jobs/jobs.html", {})

def student_Resume(request):
    return render(request, "jobs/student_resume.html", {})

def skills_List(request):
    return render(request, "jobs/skills_list.html", {})

def clients(request):
    return render(request, "jobs/clients.html", {})

def positions(request):
    return render(request, "jobs/positions.html", {})

def group_Email(request):
    return render(request, "jobs/group_email.html", {})
