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
    ordering = "id"  # = Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        template_name = "pages/index.html"
        page_size = self.get_paginate_by(self.queryset)
        paginator, page, queryset, is_paginated = self.paginate_queryset(self.queryset, page_size)
        page.number = 1
        context = {
            'paginator': paginator,  # show all range pages
            'pages': page,
            'is_paginated': is_paginated,  # check "paginate_by" field has or not
            'products': queryset  # key context transmit to html file
        }
        return render(request, template_name=template_name,context=context)

    def post(self, request):
        template= "pages/table_content.html"
        a=1
        context = {}
        render(request=request, template_name=template_name,context=context)
