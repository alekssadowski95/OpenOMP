from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class AddItemForm(FlaskForm):  
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=10)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1000)])
    item_image = FileField('Thumbnail image', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Add new item')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12, max=32)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12, max=32)])
    submit = SubmitField('Register')

class MessageForm(FlaskForm):
    text = TextAreaField('', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Send')
