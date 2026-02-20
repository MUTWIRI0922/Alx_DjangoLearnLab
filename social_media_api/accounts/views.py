from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()
# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token = Token.objects.get(user=user)
        return Response({
            'user': RegisterSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            })
        return Response(
            {"error": "Invalid Credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer

    def get_object(self):
        return self.request.user
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': RegisterSerializer(user).data
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def followuser(request, user_id):
    user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)

    if request.user == user_to_follow:
        return Response({"error": "You cannot follow yourself"}, status=400)

    request.user.following.add(user_to_follow)

    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollowuser(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)

    request.user.following.remove(user_to_unfollow)

    return Response({"message": f"You unfollowed {user_to_unfollow.username}"})