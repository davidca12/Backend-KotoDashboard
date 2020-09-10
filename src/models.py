from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



#enrollment = db.Table('enrollment',
#    db.Column('courses_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
#    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
#)


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)
    name=db.Column(db.String(120), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User")

    #enrollment = db.relationship("Enrollment", secondary=enrollment, back_populates="courses")
    
        


    def __repr__(self):
        return '<Courses %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "kotokan_id": self.kotokan_id
            
            # do not serialize the password, its a security breach
        }

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)
    name=db.Column(db.String(120), unique=True, nullable=False)

    #courses = db.relationship("Courses", secondary=enrollment, back_populates="student")

  

        


    def __repr__(self):
        return '<Student %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "kotokan_id": self.kotokan_id,
            # do not serialize the password, its a security breach
        }

      



class GameStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kotokan_id = db.Column(db.String(120), unique=True, nullable=False)
    name=db.Column(db.String(120), unique=True, nullable=False)

    

    def __repr__(self):
        return '<GameStatus %r>' % self.kotokan_id

    def serialize(self):
        return {
            "id": self.id,
            "kotokan_id": self.kotokan_id,
            # do not serialize the password, its a security breach
        }


class Enrollment(db.Model):
  

    courses_id = db.Column( db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    student_id = db.Column( db.Integer, db.ForeignKey('student.id'), primary_key=True)
    courses = db.relationship('Courses')
    students = db.relationship('Student')
    



