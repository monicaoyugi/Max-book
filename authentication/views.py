from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from authentication.serializers import RegistrationSerializer
#
# Create your views here.
class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        response_expected = {
            "user": user_data,
            "message":"user created successully"
        }
        return Response(response_expected)

