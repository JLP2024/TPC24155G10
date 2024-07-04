from datetime import datetime
from coandco import db, ma



class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(150))
    password = db.Column(db.String(25))

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f'Usuario: {self.username}'
    
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email', 'password')