from django.shortcuts import render

def app_dir(request):
    return render(request, 'django_app/app_temp.html')
