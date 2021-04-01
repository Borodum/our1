from flask import Flask, make_response, request, render_template
import datetime
from werkzeug.utils import redirect
from data import db_session, news_api, jobs_api
from data.user_model import User
from data.job_model import Jobs
from data.news_model import News
from flask_login import LoginManager, login_user
from data.logForm import LoginForm


app = Flask(__name__)
db_session.global_init('db/my_base.sqlite')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.register_blueprint(news_api.blueprint)
app.register_blueprint(jobs_api.blueprint)
# session = db_session.create_session()
# session.commit()
# hum = session.query(User).first()

login_manager = LoginManager()
login_manager.init_app(app)


def add_to_base():
    pass


def main():
    app.run(port=6503, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def ma():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/cookie')
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


if __name__ == '__main__':
    main()
