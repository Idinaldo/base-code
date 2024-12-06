import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "petshopDatabase.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_file
db = SQLAlchemy(app)


class Medico(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40), nullable=False)
    nasc = db.Column(db.DateTime, nullable=False)
    salario = db.Column(db.Float, nullable=False)
    cpf = db.Column(db.String(11), unique=True)
    telefone = db.Column(db.String(11), unique=True)
    crmv = db.Column(db.String(4), unique=True)
    email = db.Column(db.String(255), unique=True)
    dataContratacao = db.Column(db.DateTime, nullable=False)


class Tutor(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40), nullable=False)
    nasc = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(11), unique=True)
    telefone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(255), unique=True)


class Animal(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40), nullable=False)
    nasc = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    raca = db.Column(db.String(40), nullable=False)
    altura = db.Column(db.Float)
    id_tutor = db.Column(db.Integer, db.ForeignKey('Tutor.id'), nullable=False)


class Consulta(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    id_medico = db.Column(db.Integer, db.ForeignKey('Medico.id'), nullable=False)
    id_animal = db.Column(db.Integer, db.ForeignKey('Aniaml.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    dataConsulta = db.Column(db.Date, nullable=False)



# rota para index.html - homepage do petshop/projeto
@app.route('/', methods=["GET", "POST"])
def home():
    ...

# rota para login.html - página de login (tanto para médico quanto tutor)
@app.route('/login', methods=["GET", "POST"])
def login():
    ...

# rota para cadastroTutor.html - página de cadastro de tutores
@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    ...

# rota para cadastroMedico.html - página de cadastro de médicos
@app.route('/cadastroMedico', methods=["GET", "POST"])
def cadastroMedico():
    ...

# rota para cadastroAnimal.html - página de cadastro de pets/animais
@app.route('/cadastroAnimal', methods=["GET", "POST"])
def cadastroMedico():
    ...

# rota para marcarConsulta.html - página de marcação de consultas dos pets/animais
@app.route('/marcar', methods=["GET", "POST"])
def marcar():
    ...

# rota para cadastroMedico.html - página de cadastro de médicos
@app.route('/', methods=["GET", "POST"])
def d():
    ...