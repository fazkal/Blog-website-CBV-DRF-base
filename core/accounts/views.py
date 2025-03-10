from utils import EmailThreading
from serializers import RegistrationSerializer,ActivationResendSerializer
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from mail_templated import EmailMessage

User=get_user_model()
# Create your views here.

# Define view for registration account
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send token for user's email:
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_token_for_user(user_obj)
            email_obj = EmailMessage(
                "email/verify.tpl",
                {"token": token},
                "from@example.com",
                to=[email],
            )
            EmailThreading(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Create access token via refresh token for user
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# Define view for verify account's user
class ActivationApiView(APIView):

    def get(self, request, token, *args, **kwargs):
        # Decode token for get user id from jason token
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response(
                {"Details": "Token has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidSignatureError:
            return Response(
                {"Details": "Token is not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_obj = User.objects.get(pk=user_id)

        if user_obj.is_verified:
            return Response({"Details": "Your account has already been verified"})
        user_obj.is_verified = True
        user_obj.save()
        return Response(
            {"Details": "Your account have been verified and activated successfully"}
        )


# Define view for resend email of token activation account
class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivationResendSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivationResendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data["user"]
        token = self.get_token_for_user(user_obj)
        email_obj = EmailMessage(
            "email/verify.tpl",
            {"token": token},
            "from@example.com",
            to=[user_obj.email],
        )
        EmailThreading(email_obj).start()
        return Response(
            {"Details": "User activation resend successfully"},
            status=status.HTTP_200_OK,
        )

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


# logout jwt view
class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)