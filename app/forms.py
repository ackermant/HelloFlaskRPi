from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class RegInputForm(FlaskForm):
    registerno = StringField('Enter Modbus Register Number', validators=[DataRequired()])
    submit = SubmitField('Submit')
