from flask import Blueprint, render_template
from app.models import Service

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@bp.route('/services')
def services():
    return render_template('services.html')

@bp.route('/about')
def about():
    return render_template('about.html')
