from flask import Blueprint, render_template

from app.forms import Stu

student = Blueprint('student', __name__, url_prefix="/student")


@student.route('/student_registration')
def std_register():
    return render_template('students/std_register.html')