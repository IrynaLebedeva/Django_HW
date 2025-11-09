from django.http import HttpResponse

def home_page(request):
    name="Irina"
    return HttpResponse(f"Hello,{name}.")
