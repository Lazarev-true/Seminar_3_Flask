from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    date_of_birth = DateField('Дата рождения', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Повторить пароль', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Согласие на обработку пользовательских данных', validators=[DataRequired()])
