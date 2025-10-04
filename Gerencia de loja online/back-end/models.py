from flask_sqlalchemy import SQLAlchemy
from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tamanho = db.Column(db.String(20))
    categoria = db.Column(db.String(50))
    imagem = db.Column(db.String(200))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    produtos = db.Column(db.Text, nullable=False)  # Lista de IDs de produtos
    total = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)