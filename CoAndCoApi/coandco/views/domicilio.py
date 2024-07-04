from os import error
from flask import(Blueprint, flash, request, jsonify, session)
from flask_cors import CORS,cross_origin

from coandco.models.domicilio import Domicilio, DomicilioSchema
from coandco import db,ma,cr


domic = Blueprint('domic',__name__, url_prefix='/domicilios')


@cross_origin
@domic.route('/agregar', methods=['POST'])
def agregarDomicilio():
    calle = request.json['calle']
    numero = request.json['numero']
    numDepto = request.json['numDepto']
    localidad = request.json['localidad']
    provincia = request.json['provincia']
    
    domicilio = Domicilio(calle, numero, numDepto, localidad, provincia)
    if not calle :
        error = 'Se requiere nombre de la  calle'
    elif not numero:
        error = 'Se requiere Nº del domicilio'
    db.session.add(domicilio)
    db.session.commit()
    return jsonify({"message":"Domicilio agregado correctamente"})

@domic.route("/listar")
def listarTodosDomicilios():
    domicilios = Domicilio.query.all()
    print(domicilios)
    return jsonify(DomicilioSchema(many=True).dump(domicilios))

@domic.route('/listar/<id>', methods=['GET'])
def listarDomicilioId(id):
    domicilio = Domicilio.query.get(id)
    return DomicilioSchema().jsonify(domicilio)

@domic.route('/<id>', methods=['PUT'])
def actualizarDomicilio(id):
    domicilio = Domicilio.query.get(id)
    calle = request.json['calle']
    numero = request.json['numero']
    numDepto = request.json['numDepto']
    localidad = request.json['localidad']
    provincia = request.json['provincia'] 
    domicilio.calle = calle
    domicilio.numero = numero
    domicilio.numDepto = numDepto
    domicilio.localidad = localidad
    domicilio.provincia = provincia
    db.session.commit()
    return DomicilioSchema().jsonify(domicilio)