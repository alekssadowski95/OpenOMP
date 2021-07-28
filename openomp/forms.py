from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class AddItemForm(FlaskForm):  
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=10)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1000)])
    item_image = FileField('Thumbnail image', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Add')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')