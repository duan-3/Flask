from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/') # 여기서 __name__은 이 모듈의 이름인 main_views가 전달됨

@bp.route('/juan')
def hello_pybo():
    return 'hello juan'

@bp.route('/')
def index():
    return 'pybo index'
