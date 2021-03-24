from django.shortcuts import render
from .models import CustomUser
from rest_framework.response import Response

# Import the serializer
from rest_framework import status
from .serializer import CustomUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes


# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_all_user(request):
    user = CustomUser.objects.all()
    serialized_user = CustomUserSerializer(user, many=True)
    return Response(serialized_user.data)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_user(request):
    serialized_user = CustomUserSerializer(CustomUser, request.data)
    if serialized_user.is_valid():
        serialized_user.save()
        return Response(serialized_user.data)
    return Response(serialized_user.error, status=status.HTTP_400_BAD_REQUEST)
