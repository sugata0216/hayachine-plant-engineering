from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news_list_view, name="news"),
    path('news_detail/', views.news_detail, name='news_detail'),
    path("recruitment/", views.recruitment, name="recruitment"),
    path("business_activities/", views.business_activities, name="business_activities"),
    path("company_information/", views.company_information, name="company_information"),
    path("inquiry/", views.inquiry_view),
    path('news_post/', views.news_post_view)
]
