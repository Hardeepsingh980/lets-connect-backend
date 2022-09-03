from django_filters.rest_framework import DjangoFilterBackend
# rest framework
from rest_framework.viewsets import (
    GenericViewSet    
)
from rest_framework.mixins import (
    RetrieveModelMixin
)
from rest_framework.response import Response


# models imports
from users.models import (
    UserProfile,
)
from schedule.models import (
    Schedule,
)

# serializers imports
from schedule.serializers import (
    ScheduleSerializer,

)


class OpenScheduleViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'date': ['lte', 'gte']
    }
    lookup_field = 'profile_url'

    def retrieve(self, request, *args, **kwargs):
        profile_url = kwargs.get('profile_url')
        profile = UserProfile.objects.filter(profile_url=profile_url)
        if not profile.exists():
            return Response(status=404)

        profile = profile.first()
        queryset = Schedule.objects.filter(user=profile.user)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
