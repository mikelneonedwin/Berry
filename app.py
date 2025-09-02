from flask import Flask, render_template,request
from db import add_student, create_schema
import sqlite3

create_schema()

app = Flask (__name__)

@app.route("/")
def home ():
    return render_template ("index.html")


@app.route("/contact")
def contact():
    return "contact"

@app.route("/about")
def about():
    return "About"
    
@app.route("/form",methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get ("name")
        matric = request.form.get ("matric")
        add_student(name, matric)
        return "submitted successfully" 

    return render_template("form.html")

@app.route("/student/<int:id>")
def students(id):
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT name, matric FROM students
        WHERE id = ?
        """,
        (id,)
    )
    student = cursor.fetchone()
    print(student['name'])
    return render_template("student.html", name=student['name'], matric=student['matric'])
    


app.run(debug=True)