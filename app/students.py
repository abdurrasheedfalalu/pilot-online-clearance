from flask import Blueprint, render_template

from app.forms import StudentsRegisterationForm

student = Blueprint('student', __name__, url_prefix="/student")





