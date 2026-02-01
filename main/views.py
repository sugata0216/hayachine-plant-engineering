from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import *
from .forms import *

# Create your views here.

def my_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, '403.html', status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def index(request):
    news_list = News.objects.order_by('id').reverse()[:2]
    return render(request, "main/top.html", {'news_list' : news_list})
def news_list_view(request):
    news_list = News.objects.order_by('id').reverse()
    return render(request, 'main/news.html', {'news_list': news_list})
def news_detail(request, pk):
    context = News.objects.filter(id = pk)
    return render(request, 'main/news_details.html', {'context' : context})

def recruitment(request):
    return render(request, "main/recruit_ment.html")

def business_activities(request):
    return render(request, "main/business_activities.html")

def company_information(request):
    return render(request, "main/company_information.html")
 
def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            return render(request, 'main/inquiry.html', {'form' : form})
    form = InquiryForm(initial={'genre': 4})
    return render(request, "main/inquiry.html", {'form' : form})

@my_login_required
def news_post_view(request, pk=None):
    if pk:
        instance = get_object_or_404(News, pk=pk)
    else:
        instance = None
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main:news')
    else:
        if instance is None:
            form = NewsForm(initial={'genre': 1})
        else:
            form = NewsForm(instance=instance)
    return render(request, "root/news_post.html", {'form': form})

@my_login_required
def news_delete_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'ニュースを削除しました')
        return redirect('main:news')
    return render(request, 'root/news_delete.html', {'news' : news})