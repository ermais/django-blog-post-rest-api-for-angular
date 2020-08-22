from rest_framework.serializers import ModelSerializer, Serializer,CharField
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs =  {"password":{
            "write_only":True,
        }
        }
    def create(self,validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email=email,
            is_active = True,
            is_staff = True,
            is_superuser = True
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class UserLoginSerializer(Serializer):
    username = CharField()
    password = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
    def validate(self, data):
        print('validate',self,data)
        username = data.get("username")
        password = data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    print('user....')
                    data["user"] = user
                else:
                    msg = "uer is deactivated"
                    raise ValidationError(msg)
            else:
                msg = "username or password is incorrect"
                raise ValidationError(msg)
        return data
