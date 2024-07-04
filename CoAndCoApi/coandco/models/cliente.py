from datetime import datetime,date
from sqlalchemy.orm import backref
from coandco import db, ma



class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    dni=db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(200), nullable=False)
    apellido = db.Column(db.String(150), nullable=False)
    sexo = db.Column(db.Integer)
    fechaNac = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #fechaNac = db.Column(db.DateTime, server_default = db.func.now.date())
    #relacion one to one 
    idDomicilio=db.Column(db.Integer, db.ForeignKey('domicilios.id')) 
    cliente = db.relationship("Domicilio", backref = backref("cliente", uselist=False)  )  

    # relacion one to many
    ventas = db.relationship('Venta', backref = 'cliente',lazy=True)

    def __init__(self, dni, nombre, apellido, sexo, fechaNac, idDomicilio) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fechaNac = fechaNac
        self.idDomicilio = idDomicilio

    def __repr__(self) -> str:
        return f'Cliente: {self.nombre,self.apellido}'

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('dni', 'nombre', 'apellido', 'sexo', 'fechaNac', 'idDomicilio')