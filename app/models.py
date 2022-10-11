from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Staffs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    other_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    state = db.Column(db.String(20), nullable=False)
    lga = db.Column(db.String(20), nullable=False)
    staff_no = db.Column(db.String(20), nullable=False, unique=True)
    gender = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)

    def generate_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)



    def __repr__(self):
        return f'<Staff {self.first_name+ " " +self.surname}>'


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)


    def generate_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Admin {self.username}>'



class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    other_name = db.Column(db.String(20), nullable=True)
    reg_no = db.Column(db.String(20), nullable=False, unique=True)
    course_title = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    lga = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    department = db.Column(db.String(20), nullable=False)
    school = db.Column(db.String(20), nullable=False)
    reason_for_leaving = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20), nullable=False)


    def generate_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Student {self.first_name+" "+self.surname}, {self.level}, {self.department}>'
