from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# FlaskアプリがSQLAlchemyを使えるようにするための初期化
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/flask_tutorial'

    db.init_app(app)

    login_manager = LoginManager()

    # ログインマネージャーの初期ビュー設定？
    login_manager.login_view = 'auth.register'
    login_manager.init_app(app)

    from .UserModel import User

    @login_manager.user_loader
    def load_user(user_id):
        user_session = User.query.get(int(user_id))
        return user_session

    # 実行ファイル(モジュール)の分割設定(ブループリント設定)
    from .auth import auth as auth_blueprint
    from .register import register as register_blueprint
    from .show import show as show_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(show_blueprint)

    return app
