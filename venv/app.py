from flask import Flask, render_template, request, redirect, url_for
from db import db_session
from models import Pessoa

app = Flask(__name__)

@app.route('/')
def index():
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        linkedin = request.form['linkedin']
        github = request.form['github']

        nova_pessoa = Pessoa(nome=nome, email=email, linkedin=linkedin, github=github)
        db_session.add(nova_pessoa)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pessoa = Pessoa.query.get(id)

    if request.method == 'POST':
        pessoa.nome = request.form['nome']
        pessoa.email = request.form['email']
        pessoa.linkedin = request.form['linkedin']
        pessoa.github = request.form['github']

        db_session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', pessoa=pessoa)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    pessoa = Pessoa.query.get(id)

    if request.method == 'POST':
        db_session.delete(pessoa)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html', pessoa=pessoa)

if __name__ == '__main__':
    db_session.init_app(app)
    app.run(debug=True)
