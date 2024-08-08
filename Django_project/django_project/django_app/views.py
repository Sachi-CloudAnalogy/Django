from django.shortcuts import get_object_or_404, render
from .models import User

def app_dir(request):
    user = User.objects.all()
    return render(request, 'django_app/app_temp.html', {'user' : user})

def details(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'django_app/details.html', {'user': user})

