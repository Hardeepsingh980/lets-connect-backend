from schedule.models import Slots
from django.db import models

# Create your models here.
class Meeting(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)

    slot = models.ForeignKey(Slots, on_delete=models.CASCADE, related_name='meetings')
