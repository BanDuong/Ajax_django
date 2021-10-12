from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from .models import *

# Create your views here.
class index(ListView):
    # template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, template_name="pages/index.html", context=context)

    def post(self, request):
        pass
