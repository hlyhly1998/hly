from django import forms

from cb.models import User


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['name', 'password', 'email']

        labels = {'name':'用戶名', 'password':'密碼', 'email':'郵箱'}






