from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from loan.models import *


class MemberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=30)])
    id_number = StringField('Id_Number', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Save')

    def validate_id_number(self, id_number):
        member = Member.query.filter_by(id_number=id_number.data).first()
        if member:
            raise ValidationError('The id number is already registered to the system !')


class CalculatorForm(FlaskForm):
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    period = IntegerField('Period', validators=[DataRequired()])
    interest_rate = IntegerField('Interest Rate ', validators=[DataRequired()])
    submit = SubmitField('Save')


class LoanForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=30)])
    id_number = StringField('Id_Number', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(min=3, max=20)])
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    period = IntegerField('Period', validators=[DataRequired()])
    interest_rate = IntegerField('Interest Rate ', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_id_number(self, id_number):
        member = Member.query.filter_by(id_number=id_number.data).first()
        if member:
            raise ValidationError('The id number is already registered to the system !')
