from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class OrderForm(FlaskForm):
    package = SelectField(u'package', choices=[('half', 'Half Package'), ('full', 'Full Package'), ('combo', 'Combo Package'), ('special', 'Special Package')])
    firstName = StringField('Name', validators=[DataRequired()])
    lastName = StringField('Name')
    drink = SelectField(u'drink', choices=[('shakers', 'Shakers'), ('pepsi', 'Pepsi'), ('fanta', 'Fanta'), ('water', 'Water')])
    Address = StringField('adress', validators=[DataRequired()])
    email = StringField('email')
    phone = TextAreaField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    payment = SelectField(u'package', choices=[('mobile', 'Mobile Money Transfer'), ('cash', 'Cash Payment'), ('other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Search')

