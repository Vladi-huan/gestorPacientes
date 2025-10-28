from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PacienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    edad = IntegerField('Edad')
    sexo = StringField('Sexo')
    telefono = StringField('Teléfono')
    submit = SubmitField('Guardar')
