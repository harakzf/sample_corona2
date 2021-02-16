from flask import Blueprint, request, flash, url_for, redirect, render_template, session
from .UserModel import User
from flask_login import login_user, logout_user, login_required
import datetime
import hashlib

auth = Blueprint('auth', __name__)

'''
サインアップ処理
'''


'''
ログイン処理
'''
@auth.route('/register', methods=('GET', 'POST'))
def register():
    '''
    ×登録処理
    〇ログイン処理
    '''
    hash = hashlib.sha256()

    if request.method == 'POST':

        # フォームからユーザ名とパスワードを取得(パスワードは暗号化して取得)
        username = request.form['username']
        password = request.form['password']

        # 必須チェック
        error = None
        if not username:
            error = 'ユーザ名を入力して下さい。'
        elif not password:
            error = 'パスワードを入力して下さい。'
        
        # パスワードを暗号化して取得
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # ユーザ情報をDB(PostgreSQL)から取得
        userInfo = User.query.filter_by(username=username).first()

        # メッセージ格納用変数定義
        error_msg = None

        # 認証チェック
        if not userInfo or userInfo.password != password_hash:
            error_msg = 'ユーザ名またはパスワードが間違っています。'

        # 認証成功した場合            
        if error_msg is None:

            # ユーザセッション作成？
            login_user(userInfo)

            flash('ログインに成功しました。')
            return redirect(url_for('show.show_entry'))

        # 認証成功していない(失敗した)場合の処理
        else:
            flash(error_msg)
            return render_template('auth/auth_register.html')
   
    # GETリクエストの場合
    return render_template('auth/auth_register.html')

'''
ログアウト処理
'''
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.register'))
        



        
    
    
