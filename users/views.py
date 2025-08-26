from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """При создании пользователя, он сразу же активен"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        """Если действие create (создание объекта),
        то доступ к нему открыт для всех пользователей"""
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()
