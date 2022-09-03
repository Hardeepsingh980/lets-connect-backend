from rest_framework.viewsets import (
    ModelViewSet
)


# models imports
from .models import (
    Schedule
)

# serializers imports
from .serializers import (
    ScheduleSerializer
)


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)
    
