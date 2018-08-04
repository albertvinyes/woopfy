from django.contrib.auth.backends import ModelBackend
from .models import User, RegularUser

class AdminOrRegularUserBackend(ModelBackend):
    """
    Backend using ModelBackend, but attempts to "downcast"
    the user into a PersonUser or KitUser.
    """

    def authenticate(self, *args, **kwargs):
        id = kwargs.get('username')
        passwd  = kwargs.get('password')
        user = RegularUser.objects.get(email=id)
        if user.check_password(passwd):
            # Yes? return the Django user object
            return user
        else:
            # No? return None - triggers default login failed
            return None
        return user

    def get_user(self, user_id):
        print(user_id)
        try:
            user = RegularUser.objects.get(pk=user_id)
        except:
            user = None
        return user
