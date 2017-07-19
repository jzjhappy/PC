from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def Billing(request):
    return render(request, "billing/billing.html", {})

def pay_Tuition(request):
    return render(request, "billing/pay_tuition.html", {})

def payment_Notice(request):
    return render(request, "billing/payment_notice.html", {})

def sales_Log(request):
    return render(request, "billing/sales_log.html", {})
