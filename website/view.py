from flask import Blueprint,render_template

views = Blueprint('views', __name__)

@views.route('/')
def content():
    return render_template('home.html')



