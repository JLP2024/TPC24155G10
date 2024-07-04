from os import error
from flask import(Blueprint, flash, request, jsonify, session)
from flask_cors import CORS,cross_origin

from coandco.models.entrega import Entrega, EntregaSchema
from coandco import db,ma,cr


entreg = Blueprint('entreg',__name__, url_prefix='/entregas')


@cross_origin
@entreg.route('/agregar', methods=['POST'])
def agregarDomicilio():
    calle = request.json['calle']
    numero = request.json['numero']
    numDepto = request.json['numDepto']
    localidad = request.json['localidad']
    provincia = request.json['provincia']
    
    entrega = Entrega(calle, numero, numDepto, localidad, provincia)
    if not calle :
        error = 'Se requiere nombre de la  calle'
    elif not numero:
        error = 'Se requiere Nº del domicilio'
    db.session.add(entrega)
    db.session.commit()
    return jsonify({"message":"Domicilio de entrega agregado correctamente"})

@entreg.route("/listar")
def listarTodasEntregas():
    entregas = Entrega.query.all()
    return jsonify(EntregaSchema(many=True).dump(entregas))

@entreg.route('/listar/<id>', methods=['GET'])
def listarEntregaId(id):
    entrega = Entrega.query.get(id)
    return EntregaSchema().jsonify(entrega)

@entreg.route('/<id>', methods=['PUT'])
def actualizarEntrega(id):
    entrega = Entrega.query.get(id)
    calle = request.json['calle']
    numero = request.json['numero']
    numDepto = request.json['numDepto']
    localidad = request.json['localidad']
    provincia = request.json['provincia'] 
    entrega.calle = calle
    entrega.numero = numero
    entrega.numDepto = numDepto
    entrega.localidad = localidad
    entrega.provincia = provincia
    db.session.commit()
    return EntregaSchema().jsonify(entrega)