from app import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    telefono = db.Column(db.String(20))
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)
