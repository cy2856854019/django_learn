from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from repository.models import User


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        min_length=10,
        label='用户名',
        error_messages={
            'required': '输入不能为空',
        }
    )

    psw = forms.RegexField(
        r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\.\%\^\&\*\(\)])[0-9a-zA-Z!@#$\.\%\^\&\*\(\)]{8,16}$',
        max_length=16,
        min_length=8,
        label='密码',
        error_messages={
            'required': '输入不能为空',
            'invalid': '密码必须包含数字、字母、特殊字符',
            'max_length': '密码长度不能超过16位',
            'min_length': '密码长度不能少于8位',
        }
    )

    re_psw = forms.RegexField(
        r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\.\%\^\&\*\(\)])[0-9a-zA-Z!@#$\.\%\^\&\*\(\)]{8,16}$',
        max_length=16,
        min_length=8,
        label='确认密码',
        error_messages={
            'required': '输入不能为空',
            'invalid': '密码必须包含数字、字母、特殊字符',
            'max_length': '密码长度不能超过16位',
            'min_length': '密码长度不能少于8位',
        }
    )

    email = forms.EmailField(
        max_length=32,
        label='邮箱',
        error_messages={
            'required': '输入不能为空',
            'invalid': '输入格式有误',
        }
    )

    captcha = forms.CharField(
        label='验证码',
        error_messages={
            'required': '输入不能为空',
        }
    )
    save_login = forms.fields.ChoiceField(
        choices=[(False, '0'), (True, '1')],
        label="是否一周内免登录",
        required=False,
        # initial="checked",
        widget=forms.widgets.CheckboxInput,
    )

    def clean(self):
        psw = self.cleaned_data.get("psw")
        re_psw = self.cleaned_data.get("re_psw")

        if psw != re_psw:
            # 两次输入的密码不一致
            raise ValidationError("两次输入的密码不一致！")
        else:
            return self.cleaned_data

    def save(self):
        self.cleaned_data.pop('re_psw')
        self.cleaned_data.pop('captcha')
        self.cleaned_data.pop('save_login')
        obj = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if obj:
            return False
        User.objects.create(**self.cleaned_data)
        return True


class BlogForm(forms.Form):
    suffix = forms.CharField(
        max_length=32,
        min_length=10,
        label='标语',
        error_messages={
            'required': '输入不能为空',
        }
    )

    psw = forms.RegexField(
        r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\.\%\^\&\*\(\)])[0-9a-zA-Z!@#$\.\%\^\&\*\(\)]{8,16}$',
        max_length=16,
        min_length=8,
        label='密码',
        error_messages={
            'required': '输入不能为空',
            'invalid': '密码必须包含数字、字母、特殊字符',
            'max_length': '密码长度不能超过16位',
            'min_length': '密码长度不能少于8位',
        }
    )

    re_psw = forms.RegexField(
        r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\.\%\^\&\*\(\)])[0-9a-zA-Z!@#$\.\%\^\&\*\(\)]{8,16}$',
        max_length=16,
        min_length=8,
        label='确认密码',
        error_messages={
            'required': '输入不能为空',
            'invalid': '密码必须包含数字、字母、特殊字符',
            'max_length': '密码长度不能超过16位',
            'min_length': '密码长度不能少于8位',
        }
    )

    email = forms.EmailField(
        max_length=32,
        label='邮箱',
        error_messages={
            'required': '输入不能为空',
            'invalid': '输入格式有误',
        }
    )

    captcha = forms.CharField(
        label='验证码',
        error_messages={
            'required': '输入不能为空',
        }
    )
    save_login = forms.fields.ChoiceField(
        choices=[(False, '0'), (True, '1')],
        label="是否一周内免登录",
        required=False,
        # initial="checked",
        widget=forms.widgets.CheckboxInput,
    )

    def clean(self):
        psw = self.cleaned_data.get("psw")
        re_psw = self.cleaned_data.get("re_psw")

        if psw != re_psw:
            # 两次输入的密码不一致
            raise ValidationError("两次输入的密码不一致！")
        else:
            return self.cleaned_data

    def save(self):
        self.cleaned_data.pop('re_psw')
        self.cleaned_data.pop('captcha')
        self.cleaned_data.pop('save_login')
        obj = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if obj:
            return False
        User.objects.create(**self.cleaned_data)
        return True
