from django import forms


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
    }))