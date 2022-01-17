from wtforms import Form, StringField, RadioField, TextAreaField, validators
from kitExchangeCreation import Creation
from user import User


class CreateCreationForm(Form):
    name = StringField('Name: ', [validators.Length(min=1, max=50), validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    sizes = RadioField('Up to Sizes: ', choices=Creation.sizes_dict.items(), default='S')
    location = StringField('Location: ', [validators.DataRequired()])
