import pandas as pd
from flask import Flask, render_template, request
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        id = request.form["ID"]
        try:
            inp = request.form["id_value"]
            inp = int(inp)
        except:
            pass

        if id == 'student_id':
            student_data = df[df['Student id'] == inp]
            if len(student_data)<1:
                return render_template("Error.html")
            total_marks = student_data[' Marks'].sum()
            return render_template("Student Data.html", student_data=student_data, total_marks=total_marks)
        elif id =='course_id':
            course_data = df[df[' Course id'] == inp]
            if len(course_data)<1:
                return render_template("Error.html")
            average_marks = course_data[' Marks'].mean()
            maximum_marks = min(course_data[' Marks'])

            plt.hist(df[' Marks'])
            plt.savefig('static/hist.png')
            return render_template("Course Data.html", average_marks=average_marks, maximum_marks= maximum_marks)

if __name__ == "__main__":
    app.run(debug=True)