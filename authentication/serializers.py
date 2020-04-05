from rest_framework import serializers
from django.core.exceptions import ValidationError
from authentication.models import User
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    """ serilizes registration requests """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(
        max_length=12,
        min_length=6,
        write_only=True,
        error_messages={
            'min_length':'Enter a password between 6 and 12 characters long'
        }
    )
    role = serializers.ChoiceField(choices=(
        ('MA', 'MAX ADMIN'),
        ('MU', 'MAX USER'),
    ))

    confirmed_password = serializers.CharField(
        max_length=12,
        min_length=6,
        write_only=True,
        error_messages={
            'min_length':'Enter a password between 6 and 12 characters long'
        }
    )


    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password', 'confirmed_password', 'role', 'adress', 'contact']
        
    
    def validate(self, data):
        """ validate data before saving """
        confirmed_password = data.get('confirmed_password')

        try:
            validate_password(data['password'])
        except ValidationError as identifier:
            raise serializers.ValidationError({
                "password": str(identifier).replace(
                    "["", "").replace(""]", "")})

        if not self.password_match(data['password'], confirmed_password):
            raise serializers.ValidationError({
        "message":"password does not math"
        })

        return data

    def password_match(self,password1, password2):
        return password1 == password2

    def create(self, validated_data):
        del validated_data['confirmed_password']
        print(validated_data)
        return User.objects.create_user(**validated_data)
