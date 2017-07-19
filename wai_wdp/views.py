from django.shortcuts import render

def Wai_Wdp(request):
    return render(request, "wai_wdp/wai_wdp.html", {})

def search(request):
    return render(request, "wai_wdp/search.html", {})

def active_Contracts(request):
    return render(request, "wai_wdp/active_contracts.html", {})

def contracts_History(request):
    return render(request, "wai_wdp/contracts_history.html", {})

def edit_Cip(request):
    return render(request, "wai_wdp/edit_cip.html", {})

def view_Report(request):
    return render(request, "wai_wdp/view_report.html", {})