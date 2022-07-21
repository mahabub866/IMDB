from dataclasses import field
import email
from django.contrib.auth.models import User
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ('id','username','email','password','first_name', 'last_name')

        extra_kwargs = {

        'password':{'write_only': True}

        }

    def create(self, validated_data):

        password = validated_data.pop('password',None)

        user = self.Meta.model(**validated_data)

        if(password is not None):

            user.set_password(password)

            user.save()

            return user

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'error':'P1 & P2 should be Same'} )
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already use try another email'})
        
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
