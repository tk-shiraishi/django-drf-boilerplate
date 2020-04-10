from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    model = CustomUser


@api_view(["GET"])
def get_user_info(request):
    serializer = CustomUserSerializer(request.user, many=False)
    return Response(data=serializer.data, status=HTTP_200_OK)
