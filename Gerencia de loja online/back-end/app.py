from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from models import Produto, Usuario, Pedido

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    lista_produtos = [{
        'id': produto.id,
        'nome': produto.nome,
        'descricao': produto.descricao,
        'preco': produto.preco,
        'tamanho': produto.tamanho,
        'categoria': produto.categoria,
        'imagem': produto.imagem
    } for produto in produtos]
    return jsonify(lista_produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify({
        'id': produto.id,
        'nome': produto.nome,
        'descricao': produto.descricao,
        'preco': produto.preco,
        'tamanho': produto.tamanho,
        'categoria': produto.categoria,
        'imagem': produto.imagem
    })

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'], senha=dados['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201

@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    dados = request.get_json()
    novo_pedido = Pedido(
        usuario_id=dados['usuario_id'],
        produtos=','.join(map(str, dados['produtos'])),  # Converte lista de IDs em string
        total=dados['total'],
        data=datetime.now()
    )
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'mensagem': 'Pedido criado com sucesso!'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)