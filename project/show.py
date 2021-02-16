from flask import Blueprint, request, url_for, render_template
from flask_login import login_required
import datetime

show = Blueprint('show', __name__)

@show.route('/', methods=['GET'])
@login_required
def show_entry():
    '''
    登録画面表示処理を実装するモジュール
    '''

    # 本日の日付を取得
    today = datetime.date.today().strftime('%Y/%m/%d')

    # toppage.htmlを表示し、本日日付を埋め込む
    return render_template('toppage.html', currentDate=today)
