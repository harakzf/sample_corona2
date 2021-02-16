from flask_pymongo import PyMongo
from . import create_app

# mongoDBの設定メソッド
def mongo_config():
    app = create_app()

    # mongoDBサーバ設定（ローカル用）
    app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/kawamuradb'
    mongo = PyMongo(app)

    return mongo
