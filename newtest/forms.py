from django import forms
from django.forms  import fields
from django.contrib.auth.models import User

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
    check_password = fields.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':' 請輸入相同的密碼'}),
        label='確認密碼:',
        min_length=6,
    )

    first_name = fields.CharField(
        widget=forms.TextInput(attrs={'placeholder':' 請介於二到七個字之間'}),
        label='名稱:',
        min_length=2,
        max_length=10,
    )

    email = fields.CharField(
        widget=forms.TextInput(attrs={'placeholder':' '}),
        label='Email:',
        min_length=6,
    )

    def clean(self):
        username = self.cleaned_data.get('username','')
        password = self.cleaned_data.get('password','')
        first_name = self.cleaned_data.get('first_name','')
        email = self.cleaned_data.get('email','')
        check_password = self.cleaned_data.get('check_password','')

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
        
        exist = User.objects.filter(username=username).exists()

        if exist:
            raise forms.ValidationError('帳號已存在')
        
        if len(first_name)>7:
            raise forms.ValidationError('暱稱請勿超過七個字')
        
        if len(first_name)<2:
            raise forms.ValidationError('暱稱請超過兩個字')
        
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('請以@gmail.com為結尾')
        
        if password != check_password:
            raise forms.ValidationError('密碼輸入不一致')
                