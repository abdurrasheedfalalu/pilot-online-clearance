from flask import Blueprint, render_template

from app.forms import StudentsRegisterationForm

student = Blueprint('student', __name__, url_prefix="/student")



@student.route('/student_home')
def students():
    return render_template('students/students.html')


@student.route('/student_registration', methods=['GET', 'POST'])
def std_register():
    form = StudentsRegisterationForm()
    return render_template('students/std_register.html', form=form)