from flask import Blueprint, request, flash, redirect, url_for, render_template
from dateutil.parser import parse
from .MongoConfig import mongo_config
import datetime

register = Blueprint('register', __name__)

@register.route('/add', methods=['POST'])
def add_entry():
    '''
    登録処理を実装するモジュール
    '''

    # 登録フォーム(name)の内容をそれぞれ変数に格納
    billName = request.form['bills']
    workingDay = parse(request.form['workingDay'])
    temperature = request.form['temperature']

    # mongoDB登録
    mongo = mongo_config()
    mongo.db.base.insert_one({
        "billName": billName,
        "workingDay": workingDay,
        "temperature": temperature
        })

    # 登録完了後にフラッシュメッセージ生成
    flash('登録が正常に完了しました！')

    # 登録TOP画面にリダイレクト
    return redirect(url_for('show.show_entry'))

