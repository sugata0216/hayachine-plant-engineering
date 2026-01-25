from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news_list_view, name="news"),
    path('news_detail/', views.news_detail, name='news_detail'),
]