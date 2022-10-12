from flask import Blueprint, render_template, redirect, url_for, flash
from sqlalchemy import delete


from app.forms import ( AdminLoginForm, AdminRegistrationForm,
                        StaffRgistrationForm, StudentsRegisterationForm, UpdateStaffForm, UpdateStudentsForm )
from app.models import Students, db, Admin, Staffs


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
    admin = Admin.query.all()
    return render_template('admin/admin.html', admin=admin)

@bp.route('/admin_info/<int:id>')
def admin_info(id):
    admin = Admin.query.get_or_404(id)
    return render_template('admin/admin_info.html', admin=admin)

@bp.route('/admin/<int:id>/delete')
def delete_admin(id):
    admin = Admin.query.get_or_404(id)
    db.session.delete(admin)
    db.session.commit()
    return redirect(url_for('admin.adminpage'))



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



@bp.route('/staff_registration', methods=['GET', 'POST'])
def staff_reg():
    form = StaffRgistrationForm()
    if form.validate_on_submit():
        print('*' * 50)
        first_name = form.first_name.data
        surname = form.surname.data
        other_name = form.other_name.data
        dob = form.dob.data
        state = form.state.data
        lga = form.lga.data
        staff_no = form.staff_no.data
        gender = form.gender.data
        role = form.role.data
        department = form.department.data
        staff = Staffs(first_name=first_name, surname=surname, other_name=other_name,
                        dob=dob, state=state, lga=lga, staff_no=staff_no, gender=gender,
                        role=role, department=department)
        staff.generate_password(form.password.data)
        db.session.add(staff)
        db.session.commit()
        print(staff)
        flash('Your staff has been added successfully', 'success')
        return redirect(url_for('admin.staffs'))

    print(form.errors)
    return render_template('admin/staff/staff_reg.html', form=form)



@bp.route('/student_registration', methods=['GET', 'POST'])
def std_register():
    form = StudentsRegisterationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        surname = form.surname.data
        other_name = form.first_name.data
        reg_no = form.reg_no.data
        course_title = form.course_title.data
        state = form.state.data
        lga = form.lga.data
        gender = form.gender.data
        level = form.level.data
        dob = form.dob.data
        department = form.department.data
        school = form.school.data
        reason_for_leaving = form.reason_for_leaving.data
        student = Students(first_name=first_name, surname=surname, other_name=other_name,
                            reg_no=reg_no, course_title=course_title, state=state, lga=lga,
                            gender=gender, level=level, dob=dob, department=department,
                            school=school, reason_for_leaving=reason_for_leaving)
        student.generate_password(form.password.data)
        db.session.add(student)
        db.session.commit()
        flash('New student added successfully', 'success')
        return redirect(url_for('admin.students'))
    return render_template('admin/student/student_register.html', form=form)


@bp.route('/staffs')
def staffs():
    staff = Staffs.query.all()
    return render_template('admin/staff/staff.html', staff=staff)


@bp.route('/staff_info/<int:id>')
def staff_info(id):
    staff = Staffs.query.get_or_404(id)
    return render_template('admin/staff/staff_info.html', staff=staff)


@bp.route('/staff/<int:id>/update')
def update_staff_info(id):
    staff = Staffs.query.get_or_404(id)
    form = UpdateStaffForm()
    return render_template('admin/staff/update_staff_info.html', staff=staff, form=form)



@bp.route('/staff/<int:id>/delete')
def delete_staff(id):
    staff = Staffs.query.get_or_404(id)
    db.session.delete(staff)
    db.session.commit()
    return redirect(url_for('admin.staffs'))



@bp.route('/students')
def students():
    student = Students.query.all() 
    return render_template('admin/student/students.html', student=student)



@bp.route('/student_info/<int:id>')
def student_info(id):
    student = Students.query.get_or_404(id)
    return render_template('admin/student/student_info.html', student=student)


@bp.route('/student/<int:id>/update')
def update_student_info(id):
    student = Students.query.get_or_404(id)
    form = UpdateStudentsForm()
    return render_template('admin/student/update_student_info.html', student=student, form=form)



@bp.route('/student/<int:id>/delete')
def delete_student(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('admin.students'))