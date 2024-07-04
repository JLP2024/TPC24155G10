#import functools
from os import error
from flask import(Blueprint, flash, request, jsonify, session)
from flask_cors import CORS,cross_origin

from coandco.models.cliente import Cliente,ClienteSchema
from coandco import db,ma,cr


client = Blueprint('client',__name__, url_prefix='/clientes')


@cross_origin
@client.route('/agregar', methods=['POST'])
def agregarCliente():
    dni = request.json['dni']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    sexo = request.json['sexo']
    fechaNac = request.json['fechaNac']
    idDomicilio = request.json['idDomicilio']
    cliente = Cliente(dni,nombre,apellido, sexo, fechaNac, idDomicilio)
    if not nombre:
        error = 'Se requiere nombre del Cliente'
    elif not dni:
        error = 'Se requiere Nº DNI'
    db.session.add(cliente)
    db.session.commit()
    return jsonify({"message":"Cliente agregado correctamente"})

@client.route("/listar")
def listarTodosClientes():
    clientes = Cliente.query.all()
    print(clientes)
    return jsonify(ClienteSchema(many=True).dump(clientes))

@client.route('/listar/<id>', methods=['GET'])
def listarClienteId(id):
    cliente = Cliente.query.get(id)
    return ClienteSchema().jsonify(cliente)

@client.route('/<id>', methods=['PUT'])
def actualizarCliente(id):
    cliente = Cliente.query.get(id)
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    sexo = request.json['sexo']
    fechaNac = request.json['fechaNac']
    idDomicilio = request.json['idDomicilio']
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.sexo = sexo
    cliente.fechaNac = fechaNac
    cliente.idDomicilio = idDomicilio
    db.session.commit()
    return ClienteSchema().jsonify(cliente)

@client.route('/borrar/<id>', methods=['DELETE'])
def eliminarCliente(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return ClienteSchema.jsonify(cliente)
