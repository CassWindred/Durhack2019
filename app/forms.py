from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
#BooleanField, DateField, DateTimeField, DecimalField, FileField, MultipleFileField
#FloatField, IntegerField, RadioField, SelectField, SelectMultipleField
#SubmitField, StringField, HiddenField, PasswordField, TextAreaField,
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstName = StringField('First name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up!')

class SubmitInfoForm(FlaskForm):
    location = StringField('ID', default="ID from javascript plz", validators=[DataRequired()])


    submit = SubmitField('Submit')
