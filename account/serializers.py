from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','Date_Of_Birth','Name','TermsAndConditions','ContactNumber','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    #validate password and confirm password
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password!=password2:
            raise serializers.ValidationError('Passwords in both the fields do not match')
        return attrs 
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','Name','ContactNumber']