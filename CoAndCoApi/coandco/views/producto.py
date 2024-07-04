import functools
from werkzeug.utils import secure_filename

import os
import time

from os import error
from flask import(
    render_template, Blueprint, flash, g, redirect, request,jsonify, session, url_for,
    current_app)
from flask_cors import CORS,cross_origin
from flask_marshmallow import Marshmallow

from werkzeug.security import check_password_hash, generate_password_hash

from coandco.models.producto import Producto, ProductoSchema

from coandco import db,ma,cr

product = Blueprint('product', __name__, url_prefix='/productos')

#ruta_destino = './static/imagenes/'


@cross_origin
@product.route('/agregar', methods=['POST'])
def createProduct():
    nombre = request.form.get('nombre')
    codigoProducto = request.form.get('codigoProducto')
    genero = request.form.get('genero')
    talle = request.form.get('talle')
    color = request.form.get('color')
    precio = request.form.get('precio')
    stock = request.form.get('stock')
    imagen = request.files['imagen']
    nombre_imagen = ""
    # Genero el nombre de la imagen

    if imagen.filename:
        image_name = secure_filename(imagen.filename)
        nombre_base, extension = os.path.splitext(image_name) 
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        ruta_destino = current_app.config['POSTS_IMAGES_DIR']
        os.makedirs(ruta_destino, exist_ok=True)
        file_path = os.path.join(ruta_destino, nombre_imagen)
        imagen.save(file_path)

    producto = Producto(codigoProducto, nombre, genero, talle, color, nombre_imagen, precio, stock)

    if not nombre:
        error = 'Se requiere nombre del producto'
    elif not codigoProducto:
        error = 'Se requiere codigo de producto'
    db.session.add(producto)
    db.session.commit()
    return jsonify({"message":"agregado correctamente"})

@product.route("/listar")
def listarTodosProductos():
    productos = Producto.query.all()
    return jsonify(ProductoSchema(many=True).dump(productos))

@product.route('/listar/<id>', methods=['GET'])
def listarProductoId(id):
    producto = Producto.query.get(id)
    return ProductoSchema().jsonify(producto)

@product.route('/<id>', methods=['PUT'])
def actualizarProducto(id):
    print('entro',id)
    producto = Producto.query.get(id)
    nombre = request.form.get('nombre')
    codigoProducto = request.form.get('codigoProducto')
    genero = request.form.get('genero')
    talle = request.form.get('talle')
    color = request.form.get('color')
    precio = request.form.get('precio')
    stock = request.form.get('stock')
    nombre_imagen = ""
    nombre_guadado = ""
    # Verifica si se proporcionó una nueva imagen
    if request.files :
        print('paso img')
        imagen = request.files['imagen']
        nombre_imagen = ""
        # Procesamiento de la imagen
        if imagen.filename:
            image_name = secure_filename(imagen.filename)
            nombre_base, extension = os.path.splitext(image_name) 
            nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
            ruta_destino = current_app.config['POSTS_IMAGES_DIR']
            os.makedirs(ruta_destino, exist_ok=True)
            file_path = os.path.join(ruta_destino, nombre_imagen)
            # Guardar la imagen en el servidor
            imagen.save(file_path)

        # Busco el producto guardado
        producto = Producto.query.get(id)
        imagen_guardada = producto.imagen
        print(imagen_guardada)
        if producto.imagen != "": # Si existe el producto...
            imagen_vieja = producto.imagen
            # Armo la ruta a la imagen
            ruta_imagen_vieja = current_app.config['POSTS_IMAGES_DIR']
            os.makedirs(ruta_imagen_vieja, exist_ok=True)
            ruta_imagen = os.path.join(ruta_imagen_vieja, imagen_vieja)
            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    else: 
        #producto = listarProductoId(id)
        #if producto:
            #print(producto)
            nombre_imagen = request.form.get('imagen')

    producto.codigoProducto = codigoProducto
    producto.nombre = nombre
    producto.talle = talle
    producto.color = color
    producto.genero = genero
    producto.imagen = nombre_imagen
    producto.precio = precio
    producto.stock = stock
    print(type(producto.precio))
    db.session.commit()
    print('paso')
    return jsonify({"message":"actualizado correctamente"})#ProductoSchema().jsonify(producto)

@product.route('/<string:name>', methods=['GET'])
def listarProductoNombre(name):
    productos=Producto.query.filter(Producto.nombre==name).all()
    return ProductoSchema(many=True).jsonify(productos) 

@product.route('/borrar/<id>', methods=['DELETE'])
def eliminarProducto(id):
    producto = Producto.query.get(id)
    print(producto.genero)
    #Borro imagen fisica
    #imagen_guardada = producto.imagen
    if producto: # Si existe el producto...
        imagen_vieja = producto.imagen
        # Armo la ruta a la imagen
        ruta_imagen_vieja = current_app.config['POSTS_IMAGES_DIR']
        os.makedirs(ruta_imagen_vieja, exist_ok=True)
        ruta_imagen = os.path.join(ruta_imagen_vieja, imagen_vieja)
        # Y si existe la borro.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"message":"producto eliminado correctamente"})
    #ProductoSchema.jsonify(producto)




#jsonify({'message':'todo mal'})
#productos = Producto.query.filter_by(nombre=name).first()
#productos=Producto.query.filter_by(codigoProducto=2453).all()
#productos = Producto.query.get(name){
#nom = productos.nombre
#print(productos.id)
#session.clear()
#session['user_id'] = productos.id
#db.session.commit()   

