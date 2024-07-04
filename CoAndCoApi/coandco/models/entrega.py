from datetime import datetime
from sqlalchemy.orm import backref
from coandco import db, ma



class Entrega(db.Model):
    __tablename__ = 'entregas'
    id = db.Column(db.Integer, primary_key=True)
    calle = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(5), nullable=False)
    numDepto = db.Column(db.String(5))
    localidad = db.Column(db.String(150), nullable=False)
    provincia = db.Column(db.String(150), nullable=False)
    #relacion one to one 
    #idVenta=db.Column(db.integer, db.ForeingKey('ventas.id')) 
    #venta = db.relationship("Venta", backref = backref("entrega", uselist=False))    

    # relacion one to many
    ventas = db.relationship('Venta', backref = 'entrega',lazy=True)


    def __init__(self, calle, numero, localidad, provincia) -> None:
        self.calle = calle
        self.numero = numero
        self.localidad = localidad
        self.provincia = provincia

    def __repr__(self) -> str:
        return f'Entrega: {self.calle, self.numero}'

class EntregaSchema(ma.Schema):
    class Meta:
        fields = ('calle', 'numero', 'numDepto', 'localidad', 'provincia')