from django import forms
from django.core.exceptions import ValidationError
from ca_redis.models import Terminal, PortSetting


class CaPortForm(forms.Form):
    port = forms.IntegerField(min_value=1, max_value=100, label='端口')
    company_name = forms.CharField(
        max_length=64,
        label='公司全称',
        error_messages={
            'max_length': '输入超出长度',
            'require': '不能为空',
        }
    )

    terminal = forms.fields.ChoiceField(
        label="CA机柜名称",
        widget=forms.widgets.Select(),
    )

    def __init__(self, *args, **kwargs):
        super(CaPortForm, self).__init__(*args, **kwargs)
        # 将ChoiceField的choices参数写到构造函数中，这样每次创建对应的form组件对象都会从数据库里重新取一次数据，避免和数据库更新不同步
        terminal_list = Terminal.objects.values_list('id', 'name')
        self.fields['terminal'].choices = terminal_list

    def clean(self):
        '''
        全局钩子函数
        :return: 不符合筛选条件返回ValidationError， 符合则返回cleaned_data
        '''
        port = self.cleaned_data.get('port')
        terminal_id = self.cleaned_data.get('terminal')
        ret = PortSetting.objects.filter(port=port, terminal_id=terminal_id)
        ret = list(ret)
        if ret != list():
            raise ValidationError('端口{}已经被使用'.format(port))
        return self.cleaned_data

    def save(self):
        '''
        用于保存新插入的数据
        :return:
        '''
        self.cleaned_data['terminal_id'] = self.cleaned_data.pop('terminal')
        ret = PortSetting.objects.get_or_create(**self.cleaned_data)
        return ret
