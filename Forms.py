from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField
from wtforms.fields import EmailField, DateField


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField("Email", [validators.Email(), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('P', 'Public'), ('C', 'Cadet'), ('T', 'Teacher'), ('HQ', 'Headquarter')], default='P')


class UserSignUp(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField("Email", [validators.Email(), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('P', 'Public'), ('C', 'Cadet'), ('T', 'Teacher'), ('HQ', 'Headquarter')], default='P')
    password = PasswordField("Password", [validators.Length(min=6, max=15), validators.DataRequired()])
    confirmpassword = PasswordField("Confirm Password", [validators.Length(min=6, max=15), validators.DataRequired(),
                             validators.EqualTo('password', message='Passwords must match.')])


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField("Email", [validators.Email(), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('P', 'Public'), ('C', 'Cadet'), ('T', 'Teacher'), ('HQ', 'Headquarter')], default='P')


class Login(Form):
    email = EmailField("Email", [validators.Email(), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(min=6, max=15), validators.DataRequired()])
