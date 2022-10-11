from flask import Blueprint, render_template, redirect, url_for, flash


from app.forms import AdminLoginForm, StaffEmptyForm, AdminRegistrationForm
from app.models import db, Admin


bp = Blueprint('admin', __name__, url_prefix="/admin")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        adm = Admin.query.filter_by(username=form.username.data).first()
        if adm and adm.check_password(password=form.password.data):
            flash('Login successfully.', 'success')
            return redirect(url_for('admin.adminpage'))
        flash('Invalid username or password.', 'danger')
    return render_template('admin/adminlogin.html', form=form)

@bp.route('/adminpage')
def adminpage():
    form = StaffEmptyForm()
    admin = Admin.query.all()
    return render_template('admin/admin.html', form=form, admin=admin)



@bp.route('/new_admin', methods=['GET', 'POST'])
def new_admin():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        adm = Admin(username=username)
        adm.generate_password(password)
        db.session.add(adm)
        db.session.commit()
        flash(f'{username} has been created as new admin.', 'info')
        return redirect(url_for('admin.login'))

    return render_template('admin/new_admin.html', form=form)

