import pytest
from app import app, db
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:flask_password@mariadb/school_db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_listar_alunos(client):
    response = client.get('/alunos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_adicionar_aluno(client):
    aluno = {
        'nome': 'João',
        'ra': '12345'
    }
    response = client.post('/alunos', data=json.dumps(aluno), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno adicionado com sucesso!'
