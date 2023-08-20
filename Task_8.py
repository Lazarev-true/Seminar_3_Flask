# # Создать форму для регистрации пользователей на сайте. 
# # Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" 
# # и кнопку "Зарегистрироваться". При отправке формы данные должны 
# # сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from models import db, User
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        with app.app_context():
            existing_user = User.query.filter((User.name == name) | (User.email == email)).first()

            if existing_user:
                error_msg = 'Имя пользователя или адрес электронной почты уже существуют'
                form.name.errors.append(error_msg)
                return render_template('register.html', form=form)

            user = User(name=name, email=email, password=password)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        return 'Регистрация прошла успешно!'
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)