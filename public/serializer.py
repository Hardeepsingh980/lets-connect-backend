from rest_framework.serializers import (
    ModelSerializer,
    ValidationError
)

from schedule.models import (
    Slots
)
from .models import (
    Meeting,
)

class MeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
    
    def validate(self, attrs):
        super().validate(attrs)
        slot = attrs.get('slot')
        meetings = slot.meetings.all()
        print('=============================')
        print(slot)
        print(slot.max_people)
        print(meetings.count())
        if meetings.count() >= slot.max_people:
            slot.is_available = False
            slot.save()
            raise ValidationError('No more participants can join.')
        return attrs