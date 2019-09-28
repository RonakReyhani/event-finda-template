
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import authenticate
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",
                  "password1", "password2", "image")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = "__all__"


# class UsersLoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput,)

#     def __init__(self, *args, **kwargs):
#         super(UsersLoginForm, self).__init__(*args, **kwargs)
#         self.fields['email'].widget.attrs.update({
#             'class': 'form-control',
#             "name": "email"})
#         self.fields['password'].widget.attrs.update({
#             'class': 'form-control',
#             "name": "password"})

#     def clean(self, *args, **keyargs):
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")

#         if email and password:
#             user = authenticate(email=email, password=password)
#             if not user:
#                 raise forms.ValidationError("This user does not exists")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect Password")
#             if not user.is_active:
#                 raise forms.ValidationError("User is no longer active")

#         return super(UsersLoginForm, self).clean(*args, **keyargs)
