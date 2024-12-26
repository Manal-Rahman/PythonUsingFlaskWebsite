from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hi():
    return render_template("index1.html")

@app.route("/about")
def about():
    return render_template("about1.html")

@app.route("/contact")
def contact():
    return render_template("contact1.html")

@app.route("/service")
def service():
    return render_template("service1.html")

app.run(debug=True)