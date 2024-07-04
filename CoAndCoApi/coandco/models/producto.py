from datetime import datetime
from coandco import db, ma



class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    codigoProducto=db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.Integer)
    talle = db.Column(db.String(3))
    color = db.Column(db.String(15))
    imagen = db.Column(db.String(100))
    precio = db.Column(db.Float,default=0)
    stock = db.Column(db.Integer)

    def __init__(self, codigoProducto, nombre, genero, talle, color, imagen, precio, stock) -> None:
        self.codigoProducto = codigoProducto
        self.nombre = nombre
        self.genero = genero
        self.talle = talle
        self.color = color
        self.imagen = imagen
        self.precio = precio
        self.stock = stock

    def __repr__(self) -> str:
        return f'Producto: {self.nombre}'

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('codigoProducto', 'id', 'nombre', 'genero', 'talle', 'color', 'imagen', 'precio', 'stock')