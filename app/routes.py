from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.forms.paciente_form import PacienteForm
from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app.models.medico import Medico
from app import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pacientes')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@main.route('/medicos')
def listar_medicos():
    medicos = Medico.query.all()
    return render_template('medicos/listar.html', medicos=medicos)

@main.route('/consultas')
def listar_consultas():
    consultas = Consulta.query.all()
    medicos = Medico.query.all()
    return render_template('consultas/listar.html', consultas=consultas, medicos=medicos)


@main.route('/pacientes/nuevo', methods=['GET', 'POST'])
def nuevo_paciente():
    form = PacienteForm()
    if form.validate_on_submit():
        paciente = Paciente(
            nombre=form.nombre.data,
            edad=form.edad.data,
            sexo=form.sexo.data,
            telefono=form.telefono.data
        )
        db.session.add(paciente)
        db.session.commit()
        flash('Paciente registrado con éxito')
        return redirect(url_for('main.listar_pacientes'))
    return render_template('pacientes/form.html', form=form)

@main.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    form = PacienteForm(obj=paciente)
    if form.validate_on_submit():
        form.populate_obj(paciente)
        db.session.commit()
        flash('Paciente actualizado')
        return redirect(url_for('main.listar_pacientes'))
    return render_template('pacientes/form.html', form=form)

@main.route('/pacientes/eliminar/<int:id>', methods=['POST'])
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado')
    return redirect(url_for('main.listar_pacientes'))
from app.forms.medico_form import MedicoForm
from app.models.medico import Medico

@main.route('/medicos/nuevo', methods=['GET', 'POST'])
def nuevo_medico():
    form = MedicoForm()
    if form.validate_on_submit():
        medico = Medico(nombre=form.nombre.data, especialidad=form.especialidad.data)
        db.session.add(medico)
        db.session.commit()
        flash('Médico registrado')
        return redirect(url_for('main.listar_medicos'))
    return render_template('medicos/form.html', form=form)

@main.route('/medicos/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    medico = Medico.query.get_or_404(id)
    form = MedicoForm(obj=medico)
    if form.validate_on_submit():
        form.populate_obj(medico)
        db.session.commit()
        flash('Médico actualizado')
        return redirect(url_for('main.listar_medicos'))
    return render_template('medicos/form.html', form=form)

@main.route('/medicos/eliminar/<int:id>', methods=['POST'])
def eliminar_medico(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    flash('Médico eliminado')
    return redirect(url_for('main.listar_medicos'))
from app.forms.consulta_form import ConsultaForm
from app.models.consulta import Consulta

@main.route('/consultas/nueva', methods=['GET', 'POST'])
def nueva_consulta():
    form = ConsultaForm()
    if form.validate_on_submit():
        consulta = Consulta(
            id_paciente=form.id_paciente.data,
            id_medico=form.id_medico.data,
            fecha=form.fecha.data,
            diagnostico=form.diagnostico.data
        )
        db.session.add(consulta)
        db.session.commit()
        flash('Consulta registrada')
        return redirect(url_for('main.listar_consultas'))
    return render_template('consultas/form.html', form=form)

@main.route('/consultas/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    form = ConsultaForm(obj=consulta)
    if form.validate_on_submit():
        form.populate_obj(consulta)
        db.session.commit()
        flash('Consulta actualizada')
        return redirect(url_for('main.listar_consultas'))
    return render_template('consultas/form.html', form=form)

@main.route('/consultas/eliminar/<int:id>', methods=['POST'])
def eliminar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    flash('Consulta eliminada')
    return redirect(url_for('main.listar_consultas'))
