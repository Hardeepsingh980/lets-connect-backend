from rest_framework.serializers import (
    ModelSerializer,
)


from .models import (
    Meeting,
    Notify,
)


class MeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class NotifySerializer(ModelSerializer):
    class Meta:
        model = Notify
        fields = '__all__'
