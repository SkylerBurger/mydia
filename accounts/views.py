from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserSerializer


class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                token = RefreshToken.for_user(user)
                json['access_token'] = str(token.access_token)
                json['refresh_token'] = str(token)

                return Response(
                    json, 
                    status=status.HTTP_201_CREATED,
                    )
        
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST,
            )