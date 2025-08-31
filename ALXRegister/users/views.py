from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=["get"])
    def by_status(self, request):
        status = request.query_params.get("status")
        if status:
            users = UserProfile.objects.filter(status=status)
        else:
            users = UserProfile.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
