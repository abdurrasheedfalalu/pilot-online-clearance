from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, DateField, SelectField, RadioField, IntegerField
)
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length

from app.models import Admin





class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AdminRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add')

    def validate_admin(self, username):
        admin = Admin.query.filter_by(username=username.data)
        if admin:
            raise ValidationError('Admin already exists.')


class StaffEmptyForm(FlaskForm):
    Staffs = SubmitField()
    Students = SubmitField()
    add_staff = SubmitField()




class StaffRgistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('SurName', validators=[DataRequired()])
    other_name = StringField('Other Name')
    dob = DateField('Date of Birth', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired(), Length(min=3, max=10)])
    lga = StringField('L.G.A', validators=[DataRequired(), Length(min=3, max=10)])
    staff_no = StringField('Staff Number', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male','Male'), ('female', 'Female')])
    role = SelectField('Role', choices=[
        ('HOD', 'H.O.D'), ('game master', 'Game Master'),
        ('gurdian', 'Gurdian'), ('discpline master', 'Discpline Master')

    ])
    submit = SubmitField('Add')

class StaffOrStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = RadioField('Role', choices=[('student', 'Student'), ('staff', 'Staff')], default='student')
    submit = SubmitField('Submit')


class StudentsRegisterationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    surname = StringField('SurName', validators=[DataRequired()])
    other_name = StringField('Other Name')
    reg_no = StringField('Reg_no', validators=[DataRequired(), Length(max=10)])
    course_title = StringField('Course Title', validators=[DataRequired(), Length(max=10)])
    state = StringField('State', validators=[DataRequired(), Length(min=3, max=10)])
    lga = StringField('L.G.A', validators=[DataRequired(), Length(min=3, max=10)])
    gender = SelectField('Gender', choices=[('male','Male'), ('female', 'Female')])
    level = IntegerField('Level', validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    school = StringField('School', validators=[DataRequired()])
    reason_for_leaving = StringField('Reason For Leaving', validators=[DataRequired(), Length(max=20)])