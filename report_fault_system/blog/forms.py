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

    psw = forms.CharField(
        max_length=16,
        min_length=8,
        label='密码',
        validators=[RegexValidator(r'^[a-zA-Z0-9]{8,16}$', '请输入8到16位的包含字母数字的密码')],
        error_messages={
            'required': '输入不能为空',
            'invalid': '输入格式有误',
        }
    )

    re_psw = forms.CharField(
        max_length=16,
        min_length=8,
        label='确认密码',
        validators=[RegexValidator(r'^[a-zA-Z0-9]{8,16}$', '请输入8到16位的包含字母数字的密码')],
        error_messages={
            'required': '输入不能为空',
            'invalid': '输入格式有误',
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

    def clean(self):
        psw = self.cleaned_data.get("psw")
        re_psw = self.cleaned_data.get("re_psw")

        if psw != re_psw:
            self.add_error("re_psw", "两次输入的密码不一致！")
            # 两次输入的密码不一致
            raise ValidationError("两次输入的密码不一致！")
        else:
            return self.cleaned_data

    def save(self):
        self.cleaned_data.pop('re_psw')
        User.objects.create(**self.cleaned_data)
