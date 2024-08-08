from django.db import models
from django.utils import timezone

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
