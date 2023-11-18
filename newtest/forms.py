from django import forms
from django.forms  import fields

class Auth(forms.Form):
    username = fields.CharField(

        widget=forms.TextInput(attrs={'placeholder':' 帳號請大於六個字'}),
        max_length=25,


        label='帳號:',
    )

    password = fields.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' 密碼請大於六個字'}),
        label='密碼:',
        min_length=6,
    )

    def clean(self):
        username = self.cleaned_data.get('username','')
        password = self.cleaned_data.get('password','')

        if not username:
            raise forms.ValidationError('帳號不可為空')
        
        if len(username)>20:
            raise forms.ValidationError('帳號太長了')
        
        if len(username) < 6:
            raise forms.ValidationError('帳號小於六個字')
        
        if not password:
            raise forms.ValidationError('密碼不可為空')
        
        if len(password) < 6:
            raise forms.ValidationError('密碼小於六個字')