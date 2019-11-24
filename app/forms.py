from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
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
    location = StringField('ID', validators=[DataRequired()])
    accessCategory = StringField('Accessability category', default='Lights', validators=[DataRequired()])
    rating = StringField('Rating', default='5', validators=[DataRequired()])
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')


    # def __init__(self, placeId, *args, **kwargs):
    #     field = StringField('ID', default=placeId, validators=[DataRequired()])
    #     name = 'location'
    #     setattr(self, name, field)
    #     self._unbound_fields = self._unbound_fields + [[name, field]]

    #     field = StringField('Accessability category', default='Lights', validators=[DataRequired()])
    #     name = 'accessCategory'
    #     setattr(self, name, field)
    #     self._unbound_fields = self._unbound_fields + [[name, field]]

    #     field = StringField('Rating', default='5', validators=[DataRequired()])
    #     name = 'rating'
    #     setattr(self, name, field)
    #     self._unbound_fields = self._unbound_fields + [[name, field]]

    #     field = TextAreaField('Comments')
    #     name = 'comments'
    #     setattr(self, name, field)
    #     self._unbound_fields = self._unbound_fields + [[name, field]]

    #     field = SubmitField('Submit')
    #     name = 'submit'
    #     setattr(self, name, field)
    #     self._unbound_fields = self._unbound_fields + [[name, field]]

    #     super(SubmitInfoForm, self).__init__(placeId, *args, **kwargs)
    
