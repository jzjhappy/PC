from django.shortcuts import render

def Timesheet(request):
    return render(request, "timesheet/timesheet.html", {})

def attendance(request):
    return render(request, "timesheet/attendance.html", {})

def grading(request):
    return render(request, "timesheet/grading.html", {})

def advisory(request):
    return render(request, "timesheet/advisory.html", {})

def certificate(request):
    return render(request, "timesheet/certificate.html", {})

def search(request):
    return render(request, "timesheet/search.html", {})

def students_Info(request):
    return render(request, "timesheet/students_info.html", {})

def sum_Report(request):
    return render(request, "timesheet/sum_report.html", {})