# hayachine-plant-engineering
# プロジェクト名
早池峰設備工業様Webサイト作成
## 環境構築
仮想環境を作成する
python -m venv venv
仮想環境有効化
cmd(コマンドプロンプト)の場合
venv\Scripts\activate
bashの場合
source ./venv/Scripts/activate
現状インストールされているライブラリをrequirements.txtにまとめる
pip freeze > requirements.txt
requirements.txtからライブラリをインストールする
pip install -r requirements.txt
マイグレートする
python manage.py migrate
アプリを実行する
python manage.py runserver
