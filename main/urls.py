from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("recruitment/", views.recruitment, name="recruitment"),
    path("business_activities/", views.business_activities, name="business_activities"),
    path("company_information/", views.company_information, name="company_information"),
]