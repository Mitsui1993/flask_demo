from flask.ext.wtf import Form
from wtforms import StringField,BooleanField  #字符 布尔
from wtforms.validators import DataRequired   #验证 是否为空

class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)