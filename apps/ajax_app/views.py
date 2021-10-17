from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from .models import *


# Create your views here.
class index(ListView):
    queryset = Product.objects.all()
    paginate_by = 5
    # context_object_name = "products"  # key context transmit to html file
    template_name = "pages/index.html"
    ordering = "id"  # = Product.objects.all().order_by("id")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator, # show all range pages
                'pages': page,
                'is_paginated': is_paginated, # check "paginate_by" field has or not
                'products': queryset    # key context transmit to html file
            }
        else:
            context = {
                'paginator': None,
                'pages': None,
                'is_paginated': False,
                'products': queryset    # key context transmit to html file
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super().get_context_data(**context)

    # def get(self, request, *args, **kwargs):
    #     products = Product.objects.all()
    #     context = {"products": products}
    #     return render(request, template_name="pages/index.html", context=context)

    def post(self, request):
        pass
