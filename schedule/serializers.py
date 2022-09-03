from rest_framework.serializers import ModelSerializer

# models imports
from .models import Schedule, Slots


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'date')
