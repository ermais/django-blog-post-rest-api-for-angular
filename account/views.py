from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import login

# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            print('print',UserSerializer(serializer.validated_data["user"]))
            user = serializer.validated_data["user"]
            login(request, user)
            user_ser = UserSerializer(user)
            print(user_ser.data)
            token,created = Token.objects.get_or_create(user=user)
            return Response({"user":user_ser.data,"token":token.key},status=HTTP_200_OK)
        return Response(errors,status=HTTP_400_BAD_REQUEST)


