from django import forms


class TroubleForm(forms.Form):
    title = forms.CharField(
        max_length=32,
        label='标题',
        error_messages={
            'max_length': 'max_length',
            'min_length': 'min_length',
            'require': '输入不能为空',
        }
    )
    detail = forms.CharField(
        max_length=32,
        label='故障详情',
        error_messages={
            'max_length': 'max_length',
            'min_length': 'min_length',
            'require': '输入不能为空',
        }
    )
    user = forms.CharField(
        max_length=32,
        label='报障人',
        error_messages={
            'max_length': 'max_length',
            'min_length': 'min_length',
            'require': '输入不能为空',
        }
    )
    status = forms.CharField(
        max_length=32,
        label='处理状态',
        error_messages={
            'max_length': 'max_length',
            'min_length': 'min_length',
            'require': '输入不能为空',
        }
    )
    ctime = forms.DateField(
        label='报障时间',
        error_messages={
            'require': '输入不能为空',
        }
    )

