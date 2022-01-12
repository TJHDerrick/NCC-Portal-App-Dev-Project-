from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, EmailField, \
    DateField
from event import Event
from user import User


class CreateEventForm(Form):
    title = StringField('Title: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    start_date = DateField('Start Date: ', [validators.DataRequired()])
    end_date = DateField('End Date: ', [validators.DataRequired()])
    time = StringField('Time: ', [validators.DataRequired()])
    eventlocation = StringField('Location: ', [validators.DataRequired()])
    visibility = RadioField('Visibility: ', choices=Event.visibility_dict.items(), default='Y')
    sign_up_no = StringField('No of Sign Up: ', [validators.Optional()])


