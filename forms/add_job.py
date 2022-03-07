from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    title = StringField("JobTitle", validators=[DataRequired()])
    team_lead = IntegerField("Team Leader id", validators=[DataRequired()])
    work_size = StringField("Work Size", validators=[DataRequired()])
    collab = StringField("Collaborators", validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Add job')
