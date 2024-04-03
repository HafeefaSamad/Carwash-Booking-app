from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from .utils import get_token_for_user
from rest_framework import status
from rest_framework import serializers



# Create your views here.

        
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {  
                        'status':200,
                        'data':serializer.data,
                        'msg':'regidtertion sucesfully'
                    }           
                )
            return Response(
                {
                    'status':400,
                    'error':serializer.errors
                },
                status=400
            )
        
        except Exception as e:
            return Response(
                {
                    'status':500,
                    'message':'Something went wrong',
                    'error':str(e)
                },
                status=500
            )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            token = get_token_for_user(user)
            return Response(
                {
                    'status': 200,
                    'msg': 'Login Success',
                    'token': token
                }
            )
        except serializers.ValidationError as e:
            return Response(
                {
                    'status': 400,
                    'msg': 'Login Failed',
                    'error': str(e.detail)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    'status': 500,
                    'msg': 'Internal Server Error',
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(
                    {
                        'status': 200,
                        'message': 'Logout successful'
                    }
                )
            else:
                return Response(
                    {'status': 400,
                     'message': 'Refresh token not provided'
                    },
                    status=400
                )
        except Exception as e:
            return Response(
                {
                    'status': 500,
                    'error': str(e)
                },
                status=500
            )


# from django.shortcuts import render
# from rest_framework.views import APIView
# from .serializers import Userserializer
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated,AllowAny


# # Create your views here.
# class RegisterView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         try:
#             serializer = Userserializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(
#                     {
#                         'msg': 'User registered successfully',
#                         'data': serializer.data,
#                         'status': status.HTTP_201_CREATED
#                     }
#                 )
#         except Exception as e:
#             return Response(
#                 {
#                     'msg': 'Something went wrong',
#                     'error': str(e),
#                     'status': status.HTTP_400_BAD_REQUEST
#                 }
#             )
    
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             print(user)
#             if user:
#                 refresh = RefreshToken.for_user(user)
#                 return Response(
#                     {
#                         'msg': 'Login successful',
#                         'refresh': str(refresh),
#                         'access': str(refresh.access_token),
#                     },
#                     status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response(
#                     {'msg': 'Invalid credentials'},
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )
#         else:
#             return Response(
#                 {'msg': 'Please provide email and password'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
