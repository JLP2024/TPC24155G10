from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin


app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
ma = Marshmallow(app)
cr = CORS(app,resources={r"/*":{"oringins":"http://127.0.0.1:5500/"}})

#Importar vistas 
from coandco.views.cliente import client
app.register_blueprint(client)
from coandco.views.domicilio import domic
app.register_blueprint(domic)
from coandco.views.entrega import entreg
app.register_blueprint(entreg)
from coandco.views.producto import product
app.register_blueprint(product)
from coandco.views.venta import vent
app.register_blueprint(vent)

with app.app_context():
    db.create_all()