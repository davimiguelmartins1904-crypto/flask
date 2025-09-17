from flask import Blueprint
from flask import render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def pagina1():
    return render_template('pagina1.html')


@bp.route('/pagina2')
def pagina2():
 return render_template('pagina2.html')
