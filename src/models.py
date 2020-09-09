from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Courses %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "kotokan_id": self.kotokan_id,
            # do not serialize the password, its a security breach
        }

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)
  

    def __repr__(self):
        return '<Student %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "kotokan_id": self.kotokan_id,
            # do not serialize the password, its a security breach
        }

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, unique=True, nullable=False)
    student_id = db.Column(db.Integer, unique=False, nullable=False)
 

    def __repr__(self):
        return '<Enrollment %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "course": self.course_id,
            "student":self.student_id
            # do not serialize the password, its a security breach
        }

class GameStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)
    created_at = """db.Column(db.Integer, unique=False, nullable=False)"""
    data="""db.Column(db.json, unique=True, nullable=False)"""
 

    def __repr__(self):
        return '<Enrollment %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }