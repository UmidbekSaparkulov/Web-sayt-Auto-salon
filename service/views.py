from django.shortcuts import render

def serviceview(request):
    return render(request, 'services.html')
