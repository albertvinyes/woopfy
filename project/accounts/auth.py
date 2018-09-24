from django.contrib.auth.backends import ModelBackend
from .models import User, RegularUser
#from django.shortcuts import get_object_or_404

class AdminOrRegularUserBackend(ModelBackend):
    """
    Backend using ModelBackend, but attempts to "downcast"
    the user into a PersonUser or KitUser.
    """

    def authenticate(self, *args, **kwargs):
        id = kwargs.get('username')
        passwd  = kwargs.get('password')
        try:
            user = RegularUser.objects.get(pk=id)
            if user.check_password(passwd):
                # Yes? return the Django user object
                return user
        except:
            user = None
        #comment = get_object_or_404(Comment, pk=comment_id)
        return user

    def get_user(self, user_id):
        print(user_id)
        try:
            user = RegularUser.objects.get(pk=user_id)
        except:
            user = None
        return user
