# -*-coding:utf-8-*-
from django import forms


class SearchForm(forms.Form):
    CHOICES = [
        (u'ISBN', u'ISBN'),
        (u'书名', u'书名'),
        (u'作者', u'作者')
    ]

    search_by = forms.ChoiceField(
        label='',
        choices=CHOICES,
        widget=forms.RadioSelect(),
        initial=u'书名',
    )

    keyword = forms.CharField(
        label='',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': u'请输入需要检索的图书信息',
            'name': 'keyword',
        })
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label=u'手机号码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        }),
    )
    name = forms.CharField(
        label=u'名字：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'name',
            'id': 'id_name',
        }),
    )
    password = forms.CharField(
        label=u'密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'type': 'password',
            'id': 'id_password',
        }),
    )
    re_password = forms.CharField(
        label=u'重复密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 're_password',
            'id': 'id_re_password',
        }),
    )
    email = forms.CharField(
        label=u'电子邮件：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'email',
            'id': 'id_email',
        }),
        required=False,
    )

    # photo = forms.FileField(
    #     label=u'头像：',
    #     widget=forms.FileInput(attrs={
    #         'class': 'form-control',
    #         'name': 'photo',
    #         'id': 'id_photo',
    #     }),
    #     required=False,
    # )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label=u'用户名：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        })
    )
    password = forms.CharField(
        label=u'密码：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'id': 'id_password',
        }),
    )
