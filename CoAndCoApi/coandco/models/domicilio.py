from datetime import datetime
#from sqlalchemy.orm import backref
from coandco import db, ma



class Domicilio(db.Model):
    __tablename__ = 'domicilios'
    id = db.Column(db.Integer, primary_key=True)
    calle = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(5), nullable=False)
    numDepto = db.Column(db.String(5))
    localidad = db.Column(db.String(150), nullable=False)
    provincia = db.Column(db.String(150), nullable=False)
    #relacion one to one 
    #idCliente=db.Column(db.integer, db.ForeingKey('clientes.id')) 
    #cliente = db.relationship("Cliente", backref = backref("domicilio", uselist=False)) 

    def __init__(self, calle, numero, numDepto, localidad, provincia) -> None:
        self.calle = calle
        self.numero = numero
        self.numDepto = numDepto
        self.localidad = localidad
        self.provincia = provincia

    def __repr__(self) -> str:
        return f'Domicilio: {self.calle, self.numero}'

class DomicilioSchema(ma.Schema):
    class Meta:
        fields = ('calle', 'numero', 'numDepto', 'localidad', 'provincia')
        
        
