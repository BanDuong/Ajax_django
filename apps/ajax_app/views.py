from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from .models import *


# Create your views here.
class index(ListView):
    queryset = Product.objects.all()
    paginate_by = 10
    # context_object_name = "products"  # key context transmit to html file
    template_name = "pages/index.html"
    ordering = "id"  # = Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        page_size = self.get_paginate_by(self.queryset)
        paginator, page, queryset, is_paginated = self.paginate_queryset(self.queryset, page_size)
        context = {
            'paginator': paginator,  # show all range pages
            'pages': page
            ,
            'is_paginated': is_paginated,  # check "paginate_by" field has or not
            'products': queryset  # key context transmit to html file
        }
        return render(request, template_name="pages/index.html",context=context)

    def post(self, request):
        a=1
        pass
