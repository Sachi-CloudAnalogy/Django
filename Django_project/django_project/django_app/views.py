from django.shortcuts import get_object_or_404, render
from .models import User, Employee
from .forms import UserForm

def app_dir(request):
    user = User.objects.all()
    return render(request, 'django_app/app_temp.html', {'user' : user})

def details(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'django_app/details.html', {'user': user})

def form_view(request):
    employee = None
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['Employee']   #Employee from form
            employee = Employee.objects.filter(emp_name=emp)      #Employee model
    else:
        form = UserForm()
    return render(request, 'django_app/forms.html', {'employee': employee, 'form':form})
