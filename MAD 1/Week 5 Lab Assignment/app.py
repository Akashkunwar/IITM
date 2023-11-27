from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)
# db.init_app(app)
# app.app_context().push()


class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    courses = db.relationship('Course', secondary='enrollments')

    def __repr__(self):
        return '<Student %r>' % self.student_id

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey(
        'student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey(
        'course.course_id'), nullable=False)

@app.route('/', methods=['GET'])
def index():
    students = Student.query.all()
    if students:
        return render_template('index.html', students=students)
    else:
        return render_template('main.html', students=students)

# @app.route('/student/<int:student_id>/delete', methods=['GET'])
# def delete(student_id):
#     delete_student = db.session.query(
#         Student).filter_by(student_id=student_id).first()
#     delete_student.courses[:] = []
#     db.session.commit()

#     db.session.delete(delete_student)
#     db.session.commit()

#     return redirect(url_for('index'))

# @app.route('/student/<int:student_id>/', methods=['GET'])
# def view(student_id):
#     details_student = db.session.query(
#         Student).filter_by(student_id=student_id).first()

#     return render_template('view.html', student=details_student)

# @ app.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
# def update(student_id):
#     if request.method == 'GET':
#         student_details = db.session.query(
#             Student).filter_by(student_id=student_id).first()
#         print(student_details.first_name)
#         return render_template('update.html', id_student=student_id, current_roll=student_details.roll_number, current_f_name=student_details.first_name, current_l_name=student_details.last_name)
#     if request.method == 'POST':
#         first_name = request.form['f_name']
#         last_name = request.form['l_name']
#         courses_selected = request.form.getlist('courses')

#         student_update = db.session.query(
#             Student).filter_by(student_id=student_id).first()

#         # Update Values in SQL
#         student_update.first_name = first_name
#         student_update.last_name = last_name

#         print(student_update.courses)

#         student_update.courses[:] = []

#         for single_course in courses_selected:

#             course_id_add = db.session.query(Course).filter(
#                 Course.course_id == int(single_course[-1])).one()
#             student_update.courses.append(course_id_add)

#         db.session.commit()

#         return redirect(url_for('index'))

# @ app.route('/student/create', methods=['GET', 'POST'])
# def create():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        rollno = int(request.form['roll'])
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        courses_selected = request.form.getlist('courses')


        exist_check = db.session.query(
            Student).filter_by(roll_number=rollno).first()

        if exist_check:
            return render_template('exist.html')
        else:
            new_student = Student(roll_number=rollno, first_name=first_name,
                                  last_name=last_name)

            for single_course in courses_selected:

                course_id_add = db.session.query(Course).filter(
                    Course.course_id == int(single_course[-1])).one()
                new_student.courses.append(course_id_add)

            db.session.add(new_student)
            db.session.commit()

            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)