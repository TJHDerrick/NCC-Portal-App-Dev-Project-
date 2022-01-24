from wtforms import Form, StringField, RadioField, TextAreaField, validators
from productCreation import Product_Creation
from user import User


class ProductCreationForm(Form):
    name = StringField('Name: ', [validators.Length(min=1, max=50), validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    sizes = RadioField('Up to Sizes: ', choices=Product_Creation.sizes_dict.items(), default='S')
    location = StringField('Location: ', [validators.DataRequired()])

