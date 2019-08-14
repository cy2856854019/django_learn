from django.forms import Form, RadioSelect, widgets
from django.forms import fields
from manage_form import models


class ClassForm(Form):
    name = fields.CharField(max_length=18,
                            min_length=3,
                            label='班级',
                            error_messages={
                                'required': '班级不能为空',
                                'max_length': '班级输入过长',
                                'min_length': '班级输入过短',
                            })
    # teacher = fields.IntegerField(min_value=1,
    #                               label='教师',
    #                               widget=widgets.Select(choices=models.Teacher.objects.values_list('id', 'name')),
    #                               error_messages={
    #                                   'require': '老师不能为空',
    #                                   'min_value': '老师输入超出范围',
    #                               })

    # teacher = fields.ChoiceField(choices=models.Teacher.objects.values_list('id', 'name'),
    #                              label='性别',
    #                              widget=widgets.Select,
    #                              error_messages={
    #                                  'required': '性别不能为空',
    #                              })

    # teacher = fields.IntegerField(min_value=1,
    #                               label='教师',
    #                               widget=widgets.CheckboxSelectMultiple(),
    #                               error_messages={
    #                                   'require': '老师不能为空',
    #                                   'min_value': '老师输入超出范围',
    #                               })

    teacher = fields.MultipleChoiceField(label='教师',
                                         widget=widgets.SelectMultiple(),
                                         error_messages={
                                             'require': '老师不能为空',
                                             'invalid': '选择格式错误',
                                         })

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].widget.choices = models.Teacher.objects.values_list('id', 'name')


class TeacherForm(Form):
    name = fields.CharField(max_length=32,
                            min_length=2,
                            label='姓名',
                            error_messages={
                                'required': '姓名不能为空',
                                'max_length': '姓名输入过长',
                                'min_length': '姓名输入过短',
                            })

    age = fields.IntegerField(max_value=60,
                              min_value=18,
                              label='年龄',
                              error_messages={
                                  'required': '老师不能为空',
                                  'invalid': '年龄必须为整数',
                                  'max_value': '年龄过大',
                                  'min_value': '年龄过小',
                              })

    CHOICES = [(0, '男'),
               (1, '女')]
    gender = fields.ChoiceField(choices=CHOICES,
                                label='性别',
                                widget=RadioSelect,
                                error_messages={
                                    'required': '性别不能为空',
                                })
