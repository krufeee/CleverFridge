from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'gender')
        field_classes = {
            'username': UsernameField,
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'gender')
        field_classes = {"username": UsernameField}
