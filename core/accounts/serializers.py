from models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers


# Define Serializer for registration account
class RegistrationSerializer(serializers.ModelSerializer):
    # For confirm password:
    password1 = serializers.CharField(max_length=225, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"Detail": "Passwords does not match"})

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return User.objects.create_user(**validated_data)
    

# Define Serializer for resend activation token
class ActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"Details": "User does not exist"})
        if user_obj.is_verified:
            raise serializers.ValidationError(
                {"Detail": "User is already activated and verified"}
            )
        attrs["user"] = user_obj
        return super().validate(attrs)