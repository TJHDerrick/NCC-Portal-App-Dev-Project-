from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, EmailField, \
    DateField, TimeField, IntegerField, BooleanField
from event import Event, SignUp
from user import User
import shelve

db_name = 'library'
db_events_key = 'events'


def get_event_list():
    event_dict = {}
    db = shelve.open(db_name)
    if db_events_key in db:
        event_dict = db[db_events_key]
    db.close()
    return event_dict.values()


# make a variable for get_event_list
# name variable eventList
# create new dictionary as eventsForm key = event shortform: value = event name
eventname_dict = {
    '': 'Select', 'NDP': 'National Day Parade', 'KM': 'Konfrontasi Memorial', 'CAMP': 'NCC Camp'
}

eventList = get_event_list()
for event in eventList:
    eventname_dict[event.get_shortform()] = event.get_title()


class CreateEventForm(Form):
    shortform = StringField('Shortform: ', [validators.DataRequired()])
    title = StringField('Title: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    start_date = DateField('Start Date: ', [validators.DataRequired()])
    end_date = DateField('End Date: ', [validators.DataRequired()])
    time = TimeField('Time: ', [validators.DataRequired()])
    eventlocation = StringField('Location: ', [validators.DataRequired()])
    visibility = RadioField('Visibility: ', choices=Event.visibility_dict.items(), default='Y')
    sign_up_no = IntegerField('No of Sign Up: ', [validators.Optional()])

    def validate_on_submit(self):
        result = super(CreateEventForm, self).validate()
        if self.start_date.data > self.end_date.data:
            return False
        else:
            return result


class SignUpForm(Form):
    eventname = SelectField('Choose event', [validators.DataRequired()], choices=eventname_dict.items())
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    nric = StringField('NRIC',
                       [validators.Regexp('^[SsTtFfGg][0-9]{7}[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]$'),
                        validators.DataRequired()])
    school = SelectField('School', [validators.DataRequired()], choices=SignUp.school_dict.items(), default='')
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    awareness = BooleanField('I am aware', [validators.InputRequired()])
    notification = RadioField('Notification: ', choices=SignUp.notification_dict.items(), default='Y')
