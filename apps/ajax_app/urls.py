from django.urls import path
from .views import *

app_name = "ajax_app"

urlpatterns =[
    path('index/', index.as_view()),
]