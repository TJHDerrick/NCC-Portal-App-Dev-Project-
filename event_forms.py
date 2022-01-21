from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, EmailField, \
    DateField, TimeField, IntegerField, BooleanField
from event import Event, SignUp
from user import User


class CreateEventForm(Form):
    title = StringField('Title: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    start_date = DateField('Start Date: ', [validators.DataRequired()])
    end_date = DateField('End Date: ', [validators.DataRequired()])
    time = TimeField('Time: ', [validators.DataRequired()])
    eventlocation = StringField('Location: ', [validators.DataRequired()])
    visibility = RadioField('Visibility: ', choices=Event.visibility_dict.items(), default='Y')
    sign_up_no = IntegerField('No of Sign Up: ', [validators.Optional()])


class SignUpForm(Form):
    eventname = RadioField('Choose event', [validators.DataRequired()], choices=SignUp.eventname_dict.items())
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    nric = StringField('NRIC', [validators.Length(min=1, max=9), validators.DataRequired()])
    school = SelectField('School', [validators.DataRequired()], choices=SignUp.school_dict.items(), default='')
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    awareness = BooleanField('I am aware', [validators.InputRequired()])
    notification = RadioField('Notification: ', choices=SignUp.notification_dict.items(), default='Y')
