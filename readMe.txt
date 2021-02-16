■本プロジェクトの実行方法
$ cd ./sample-corona（sample-coronaディレクトリ直下に移動）
$ python manage.py


■Python仮想環境の作成方法
※前提：ローカル環境にPython3.Xがインストールされていること。

$ cd ./sample-corona（sample-coronaディレクトリ直下に移動）
$ python -m venv venv
$ cd ./venv/Scripts
$ activate
$ cd ../../
$ pip install -r requirements.txt

■認証機能実装における参考サイト
https://qiita.com/penpenta/items/f40624a2b70ae6425ef8



■アプリ初期実行時の設定
・仮想環境上で以下環境変数を設定
(vemv)$ set FLASK_APP=project
(vemv)$ set FLASK_DEBUG=1

FLASK_APP：アプリケーションをロードする方法を記載。
　これは、create_app の場所を指します。ここでは、プロジェクトディレクトリを指します。

FLASK_DEBUG ：1に設定することで、ブラウザでアプリケーションエラーを表示するデバッガを有効にする


・アプリ実行
※flask_auth_appディレクトリにいること。
(vemv)$ flask run

■最新断面
・manage.pyはいらない

■優先度高タスク
・こちらの認証資材と、BXO側の参照資材をマージ
・postgresqlコンテナ作成
・サインアップ処理の追加

===サーバ側とクライアント側===

・ヘッダ部分の出し分け方法

・行動詳細タブの項目登録方法
・パスワードフォームがおかしい


■その他(gitコマンド)
・現在のリモートURLの確認
$ git remote -v

・リモートURLの変更
$ git remote set-url origin <URL>

■git config確認
git config user.name
git config user.email

■git config変更
git config --global user.name <アカウント名>
