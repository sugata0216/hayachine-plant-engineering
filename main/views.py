from django.shortcuts import render

# Create your views here.

def recruitment(request):
    return render(request, "main/recruit_ment.html")

def business_activities(request):
    return render(request, "main/business_activities.html")

def company_information(request):
    return render(request, "main/company_information.html")