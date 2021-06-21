from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is the homepage (/)")
    return render(request, 'home.html')