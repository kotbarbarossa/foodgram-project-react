from djoser.serializers import UserSerializer
from users.models import User


class UserSerializer(UserSerializer):
    
    class Meta:
        model = User
        fields = (
            'id', 'email', 'username',
            'first_name', 'last_name', 'password',)

