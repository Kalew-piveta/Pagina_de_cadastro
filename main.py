from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp, InputRequired
import csv



class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[
        InputRequired(message='O nome é obrigatório.'),
        Regexp(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', flags=0, message='O nome deve conter apenas letras.')])
    
    sobrenome = StringField('Sobrenome', validators=[
    InputRequired(message='O sobrenome é obrigatório.'),
    Regexp(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', flags=0, message='O sobrenome deve conter apenas letras.')])

    cpf = StringField('CPF', validators=[
    Length(min=11, max=11, message='O CPF deve ter exatamente 11 dígitos.'),
    Regexp(r'^\d{11}$', message='O CPF deve conter apenas números.')])
    
    email = StringField('Email', validators=[DataRequired(), Email(message='Email inválido. Por favor, coloque em um formato válido: exemplo123@domínio.com')])
    
    telefone = StringField('Telefone', validators=[Regexp(r'^\(\d{2}\)\s\d{5}-\d{4}$', message='Formato inválido de telefone. Exemplo: (XX) XXXXX-XXXX')])

    # Adicione outros campos do formulário conforme necessário

    submit = SubmitField('Cadastrar')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f2rf9IqLanFg7AQ6t3011La84xAvMT0pwA4Z5rWz'


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()

    if form.validate_on_submit():
        # Obter os dados do formulário
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        email = form.email.data
        telefone = form.telefone.data
        cpf = form.cpf.data

        # Escrever os dados no arquivo CSV
        with open('cadastros.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, sobrenome, email, telefone, cpf])

        return redirect(url_for('success'))

    return render_template('cadastro.html', form=form)

@app.route('/success')
def success():
    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)