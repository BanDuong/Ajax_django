from django.urls import path
from .views import *

app_name = "custom_page_errors"

urlpatterns =[
    path('', custom_page_404),
]