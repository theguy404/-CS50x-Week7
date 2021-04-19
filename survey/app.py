import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    fname = request.form.get("fname")
    lname = request.form.get('lname')
    house = request.form.get('house')
    position = request.form.get('position')
    
    # Confirms user data
    if not fname or not lname or not house or not position:
        # If user data is not correct send user to error
        if not fname:
            return render_template("error.html", message="First name missing.")
        elif not lname:
            return render_template("error.html", message="Last name missing.")
        elif not house:
            return render_template("error.html", message="Please select a house.")
        elif not position:
            return render_template("error.html", message="Please choose your Quiddatch position")
    else:
        # If user data is correct post data and send user to sheets
        with open('survey.csv', "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([fname, lname, house, position])
        return redirect("/sheet")
    


@app.route("/sheet", methods=["GET"])
def get_sheet():
    students = []
    with open("survey.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            students.append(row)
    return render_template("sheets.html", students=students)
