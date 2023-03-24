from django.shortcuts import render

# Create your views here.
def generic_static(request):
    return render(request,'monkey.html')