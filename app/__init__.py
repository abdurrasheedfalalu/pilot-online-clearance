from flask import Flask, render_template

from app.staffs import staff
from app.students import student
from app.admin import bp
from app.models import db
from config import Config
from app.forms import StaffOrStudentForm

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        form = StaffOrStudentForm()
        return render_template('index.html', form=form)
    

    if test_config:
        app.config.from_mapping(test_config)

    db.init_app(app)

    app.register_blueprint(bp)
    app.register_blueprint(staff)
    app.register_blueprint(student)






    

    return app