# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField(u'邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;箱:', validators=[Required(), Length(1, 64), Email()], render_kw={"placeholder": "yourname@example.com",
                        "style": "background: url(/static/login-locked-icon.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    password = PasswordField(u'密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码:', validators=[Required()], render_kw={"placeholder": "Your Password",
                        "style": "background: url(/static/password-icon.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    remember_me = BooleanField(u'记住我', render_kw={"style": "align:right; text-indent: 28px;"})
    submit = SubmitField(u'登    录', render_kw={"style": "width:282px; height:40px; background-color:#126fda; font-weight:bold;"})


class RegistrationForm(Form):
    email = StringField(u'邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;箱:', validators=[Required(), Length(1, 64), Email()], render_kw={"placeholder": "yourname@example.com",
                        "style": "background: url(/static/login-locked-icon.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    username = StringField(u'用户名:', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          u'用户名只能包括字母数字小数点和下划线')], render_kw={"placeholder": "Your Name",
                        "style": "background: url(/static/username.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    #remember_me = BooleanField(u'&nbsp;&nbsp;记住我', default=False, render_kw={"style": "text-indent: 0px; align:left;"})
    password = PasswordField(u'密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码:', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须相同!')], render_kw={"placeholder": "Your Password",
                        "style": "background: url(/static/password-icon.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    #remember_me = BooleanField(u'&nbsp;&nbsp;记住我', default=False, render_kw={"style": "text-indent: 0px; align:left;"})
    password2 = PasswordField(u'确认密码:', validators=[Required()], render_kw={"placeholder": "Your Password",
                        "style": "background: url(/static/password-icon.png)no-repeat 15px center; text-indent: 28px; height:35px; width:280px; border-width:1px"})
    #remember_me = BooleanField(u'&nbsp;&nbsp;记住我', default=False, render_kw={"style": "text-indent: 0px; align:left;"})
    submit = SubmitField(u'注    册', render_kw={"style": "width:282px; height:40px; background-color:#126fda; font-weight:bold;"})

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已经被注册!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'该用户已存在!')


class ChangePasswordForm(Form):
    old_password = PasswordField(u'旧密码', validators=[Required()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须相同')])
    password2 = PasswordField(u'确认新密码', validators=[Required()])
    submit = SubmitField(u'更新密码')


class PasswordResetRequestForm(Form):
    email = StringField(u'邮     箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField(u'重置密码')


class PasswordResetForm(Form):
    email = StringField(u'邮     箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'密    码', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须相同')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError(u'未注册的邮箱')


class ChangeEmailForm(Form):
    email = StringField(u'更改邮箱', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField(u'密    码', validators=[Required()])
    submit = SubmitField(u'确认更改邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已被注册')
