from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from accounts.models.user import User
from accounts.serializers.user import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

class UserLoginAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email, password=password)
            if not user:
                return Response({'message':'Invalid email or password'}, status=400)
            if user:
                refresh = RefreshToken.for_user(user)
                token = {'refresh': str(refresh),'access': str(refresh.access_token),}
                return Response(token)
            else:
                pass
        except User.DoesNotExist:
            return Response({'message':'User does not exist'})
