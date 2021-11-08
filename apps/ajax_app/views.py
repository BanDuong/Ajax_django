from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
import json
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
        context = {
            'paginator': paginator,  # show all range pages
            'pages': page,
            'is_paginated': is_paginated,  # check "paginate_by" field has or not
            'products': queryset  # key context transmit to html file
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request):
        template_name = "pages/table_content.html"
        data = json.loads(request.body.decode("utf-8"))
        # current_page_id = data['current_page_id']

        paginator, page = self.Create_paginator(data)
        context = {
            'paginator': paginator,  # show all range pages
            'pages': page,
            'is_paginated': page.has_other_pages(),  # check "paginate_by" field has or not
            'products': page.object_list  # key context transmit to html file
        }
        return render(request=request, template_name=template_name, context=context)


    def Create_paginator(self, data):
        page_size = self.get_paginate_by(self.queryset)
        paginator = self.get_paginator(
            self.queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page = data.get("id_next_or_pre")
        page = paginator.page(page)

        return paginator, page
