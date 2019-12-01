from django.urls import path
from Apps.Principal.views import home

app_name="Principal"

urlpatterns = [
    path('', home, name="home"),
]