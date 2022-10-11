from flask import Blueprint, flash, redirect, render_template, url_for

from app.models import Staffs, db
from app.forms import StaffRgistrationForm

staff = Blueprint('staff', __name__, url_prefix="/staffs")


@staff.route('/home')
def index():
    return render_template('staffs/staff.html')



@staff.route('/staff_registration', methods=['GET', 'POST'])
def staff_reg():
    form = StaffRgistrationForm()
    if form.validate_on_submit():
        flash('Your staff has been added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('staffs/staff_reg.html', form=form)