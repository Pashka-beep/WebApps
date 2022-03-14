from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    title = StringField("Название работы", validators=[DataRequired()])
    team_lead = IntegerField("Id Тимлидера", validators=[DataRequired()])
    work_size = StringField("Размер работы", validators=[DataRequired()])
    collab = StringField("Коллабораторы", validators=[DataRequired()])
    is_finished = BooleanField('Закончена работа?')
    submit = SubmitField('Добавить работу')
