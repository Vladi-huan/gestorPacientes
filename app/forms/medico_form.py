from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MedicoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    especialidad = StringField('Especialidad')
    submit = SubmitField('Guardar')
