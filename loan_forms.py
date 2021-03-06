from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, EmailField, \
    DateField, IntegerField, TelField
from event import Event
from loan import Loan


class CreateLoanForm(Form):
    email = EmailField('Email: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    number = IntegerField('Number: ', [validators.NumberRange(min=10000000, max=98999999, message="Stop"), validators.DataRequired(message="Stop")])
    date = DateField('Date: ', [validators.DataRequired()])
    choice = SelectField('Loan Choice', [validators.DataRequired()], choices=Loan.choice_dict.items(), default='')

class UpdateLoanForm(Form):
    email = EmailField('Email: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    number = IntegerField('Number: ', [validators.NumberRange(min=10000000, max=98999999, message="Stop"), validators.DataRequired(message="Stop")])
    date = DateField('Date: ', [validators.DataRequired()])
    choice = SelectField('Loan Choice', [validators.DataRequired()], choices=Loan.choice_dict.items(), default='')
