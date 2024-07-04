from os import error
from flask import(Blueprint, flash, request, jsonify, session)
from flask_cors import CORS,cross_origin

from coandco.models.venta import Venta, VentaSchema
from coandco import db,ma,cr


vent = Blueprint('vent',__name__, url_prefix='/ventas')


@cross_origin
@vent.route('/agregar', methods=['POST'])
def agregarVenta():
    fecha = request.json['fecha']
    importe = request.json['importe']
    idEntrega = request.json['idEntrega']
    idCliente = request.json['idCliente']
    
    venta = Venta(fecha, importe, idEntrega, idCliente)
    if not idCliente :
        error = 'Se requiere nombre del Cliente'
    elif not idEntrega:
        error = 'Se requiere domicilio de entrega'
    db.session.add(venta)
    db.session.commit()
    return jsonify({"message":"Domicilio de entrega agregado correctamente"})

@vent.route("/listar")
def listarTodasVentas():
    ventas = Venta.query.all()
    return jsonify(VentaSchema(many=True).dump(ventas))

@vent.route('/listar/<id>', methods=['GET'])
def listarVenteId(id):
    venta = Venta.query.get(id)
    return VentaSchema().jsonify(venta)

@vent.route('/<id>', methods=['PUT'])
def actualizarVenta(id):
    venta = Venta.query.get(id)
    fecha = request.json['fecha']
    importe = request.json['importe']
    idEntrega = request.json['idEntrega']
    idCliente = request.json['idCliente']
    venta.fecha = fecha
    venta.importe = importe
    venta.idEntrega = idEntrega
    venta.idCliente = idCliente
    db.session.commit()
    return VentaSchema().jsonify(venta)