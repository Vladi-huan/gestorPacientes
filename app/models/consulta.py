from app import db

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.Text)
