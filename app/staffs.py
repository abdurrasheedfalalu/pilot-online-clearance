from flask import Blueprint, render_template
from app.forms import StaffRgistrationForm, StaffEmptyForm

staff = Blueprint('staff', __name__, url_prefix="/staffs")


@staff.route('/home', methods=['GET', 'POST'])
def index():
    form = StaffEmptyForm()
    return render_template('staffs/staff.html', form=form)



@staff.route('/staff_reg', methods=['GET', 'POST'])
def staff_reg():
    form = StaffRgistrationForm()
    return render_template('staffs/staff_reg.html', form=form)