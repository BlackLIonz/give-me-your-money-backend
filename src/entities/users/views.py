from rest_framework import generics, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from common.permision_system import ActionBasedPermission
from entities.users.models import User
from entities.users.serializer import TokenObtainPairSerializer, UserSerializer


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    permission_classes = (ActionBasedPermission,)
    serializer_class = UserSerializer
    action_permissions = {
        AllowAny: ['create', 'list'],
        IsAuthenticated: ['me'],
    }

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request, **kwargs):
        serializer_data = UserSerializer(request.user).data
        return Response(serializer_data, status=status.HTTP_200_OK)
