from django.shortcuts import render, HttpResponse

# Create your views here.
# URL dispather example is below,
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is the service page")

# We will now see example of static and template.