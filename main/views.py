from django.shortcuts import render


# Create your views here.
def inquiry_view(request):
    return render(request, "main/inquiry.html")
