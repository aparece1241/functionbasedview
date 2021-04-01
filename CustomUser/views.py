from django.contrib.auth.context_processors import auth

from .models import CustomUser
from rest_framework.response import Response
import json

from django.contrib.auth.hashers import make_password

# Import the serializer
from rest_framework import status
from .serializer import CustomUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes


# read this : https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html#how-jwt-works

# Create your views here.


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@renderer_classes([JSONRenderer])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def user_action(request, pk=None):
    response = {}
    data = {}
    try:
        if pk:
            user = CustomUser.objects.get(pk=pk)
            data = CustomUserSerializer(user, many=False)
        if request.method == 'GET' and not pk:
            users = CustomUser.objects.all()
            data = CustomUserSerializer(users, many=True)
        if request.method == 'POST':
            user = CustomUser()
            data = CustomUserSerializer(user, request.data)
            if not data.is_valid():
                response['message'] = 'Something wrong'
                response['error'] = True
                response['data'] = {}
                response['status'] = status.HTTP_408_REQUEST_TIMEOUT
            data.save()
            data = user
        if request.method == 'PATCH' and pk:
            user = CustomUser.objects.filter(id=pk)
            payload = json.loads(request.body)
            if payload['password']:
                payload['password'] = make_password(payload['password'])
            user.update(**payload)
            data = user
        if request.method == 'DELETE':
            user.delete()
            data = user

        response['message'] = 'Success'
        response['status'] = status.HTTP_200_OK
        response['data'] = data.data
        response['error'] = False
    except:
        response['message'] = 'Something wrong'
        response['status'] = status.HTTP_409_CONFLICT
        response['error'] = True
        response['data'] = {}

    return Response(response, status=response['status'])

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# @authentication_classes([JWTTokenUserAuthentication])
# @permission_classes([IsAuthenticated])
# def get_all_user(request):
#     user = CustomUser.objects.all()
#     serialized_user = CustomUserSerializer(user, many=True)
#     return Response(serialized_user.data)
#
#


# @api_view(['GET'])
# @authentication_classes([JWTTokenUserAuthentication])
# @renderer_classes([JSONRenderer])
# @permission_classes([IsAuthenticated])
# def get_user_by_id(request, id):
#     response = {}
#     serialized_user = ''
#     try:
#         user = CustomUser.objects.get(id=id)
#         serialized_user = CustomUserSerializer(user, many=False)
#         response['error'] = False
#         response['message'] = 'Success'
#         response['data'] = serialized_user.data
#     except:
#         response['error'] = True
#         response['message'] = 'Unknown id '+ id
#         response['data'] = []
#
#     return Response(response)
#
# @api_view(['POST'])
# @authentication_classes([JWTTokenUserAuthentication])
# @renderer_classes([JSONRenderer])
# @permission_classes([IsAuthenticated])
# def add_user(request):
#     response = {}
#     user = CustomUser()
#     print(request.data)
#     serialized_user = CustomUserSerializer(user, request.data)
#     if serialized_user.is_valid():
#         serialized_user.save()
#         response['error'] = False
#         response['message'] = 'successfully added!'
#         response['data'] = serialized_user.data
#         return Response(response)
#     return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT'])
# @authentication_classes([JWTTokenUserAuthentication])
# @renderer_classes([JSONRenderer])
# @permission_classes([IsAuthenticated])
# def update_user(request, id):
#     response = {}
#     try:
#         user = CustomUser.objects.filter(id=id)
#         payload = json.loads(request.body)
#         if payload['password']:
#             payload['password'] = make_password(payload['password'])
#         user.update(**payload)
#         response['message'] = 'Success'
#         response['error'] = False
#         response['status'] = status.HTTP_200_OK
#     except:
#         response['error'] = True
#         response['message'] = 'Something went wrong'
#         response['status'] = status.HTTP_400_BAD_REQUEST
#
#     return Response(response, status=response['status'])
