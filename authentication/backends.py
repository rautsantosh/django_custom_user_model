from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackendModel(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            print(f"username = {username}")
            print(f"password = {password}")
            print(f"**kwargs = {kwargs}")
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


