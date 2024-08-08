from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User  (default user by django)

# Create your models here.
class User(models.Model):
    Days = [('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=timezone.now)
    day = models.CharField(max_length=3, choices=Days)
    city = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emp_name')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)   if we want to use django's user table
    post = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.emp_name.name}({self.emp_name.city}) -- {self.post}'
