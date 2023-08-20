# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms2 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        flash('Регистрация прошла успешно!')
        return redirect(url_for('success'))
    
    return render_template('registration.html', form=form)

@app.route('/success/')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
