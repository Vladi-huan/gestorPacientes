from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from app.models.paciente import Paciente
from app.models.medico import Medico

class ConsultaForm(FlaskForm):
    id_paciente = SelectField('Paciente', coerce=int, validators=[DataRequired()])
    id_medico = SelectField('Médico', coerce=int, validators=[DataRequired()])
    fecha = DateField('Fecha', validators=[DataRequired()])
    diagnostico = TextAreaField('Diagnóstico')
    submit = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_paciente.choices = [(p.id, p.nombre) for p in Paciente.query.all()]
        self.id_medico.choices = [(m.id, m.nombre) for m in Medico.query.all()]
