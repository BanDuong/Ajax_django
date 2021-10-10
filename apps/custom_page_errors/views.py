from django.shortcuts import render


# Create your views here.

def custom_page_404(request, exception):
    return render(request, template_name="errors/page_404.html", context={}, status=404)
