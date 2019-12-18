from django import forms
from django.forms import widgets, fields
from repository.models import User, Trouble


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
        widget=widgets.Textarea,
        label='故障详情',
        error_messages={
            'max_length': 'max_length',
            'min_length': 'min_length',
            'require': '输入不能为空',
        }
    )
    user = fields.ChoiceField(
        widget=widgets.Select,
        label='报障人',
        error_messages={
            'require': '输入不能为空',
        }
    )
    ctime = forms.DateTimeField(
        widget=widgets.SelectDateWidget,
        label='报障时间',
        error_messages={
            'require': '输入不能为空',
        }
    )

    def __init__(self, *args, **kwargs):
        super(TroubleForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = User.objects.all().values_list('id', 'username')

    def save(self, trouble_id):
        self.cleaned_data['user_id'] = self.cleaned_data.pop('user')
        if trouble_id == 0:
            Trouble.objects.create(**self.cleaned_data)
        else:
            num = Trouble.objects.filter(id=trouble_id, status=1).update(**self.cleaned_data)
            if num == 0:
                return False
        return Trouble
