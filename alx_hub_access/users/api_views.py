from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users': reverse('user-list-create', request=request, format=format),
    })
