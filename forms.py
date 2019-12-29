from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateLockForm(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    pros = TextAreaField('Pros (one per line)', validators=[DataRequired()])
    cons = TextAreaField('Cons (one per line)', validators=[DataRequired()])
    submit = SubmitField('Add Lock')


class UpdateLockForm(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    pros = TextAreaField('Pros (one per line)', validators=[DataRequired()])
    cons = TextAreaField('Cons (one per line)', validators=[DataRequired()])
    submit = SubmitField('Update Lock')


class ConfirmDelete(FlaskForm):
    brand = StringField('Brand', validators=[DataRequired()])
    submit = SubmitField('Delete this Lock')
