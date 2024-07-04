from datetime import datetime
from sqlalchemy import Table
from coandco import db,ma


association_table = Table(
    "detalle_venta",
    db.metadata,
    db.Column("idVenta", db.ForeignKey("ventas.id"), primary_key=True),
    db.Column("idProducto", db.ForeignKey("productos.id"), primary_key=True),
)

class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    importe = db.Column(db.Float,nullable=False) 
    idEntrega = db.Column(db.Integer,db.ForeignKey('entregas.id'))
    idCliente=db.Column(db.Integer, db.ForeignKey('clientes.id'))   
    
    def __init__(self, fecha, importe, idEntrega, idCliente) -> None:
        self.fecha = fecha
        self.importe = importe
        self.identrega = idEntrega
        self.idCliente = idCliente

    def __repr__(self) -> str:
        return f'Venta: {self.id, self.fecha}'

class VentaSchema(ma.Schema):
    class Meta:
        fields = ('fecha', 'importe', 'idEntrega', 'idCliente')