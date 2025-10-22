from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        try:
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])
            
            today = date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))
        except ValueError:
            age = "Invalid input. Please enter valid numbers."
    
    return render_template("index.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
