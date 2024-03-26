from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def lendingpage():
    return render_template("index.html")

@app.route("/skincare")
def skincare():
    return render_template("skincare.html")


@app.route("/routines")
def routines():
    return render_template("routines.html")

@app.route("/ingredients")
def ingredients():
    return render_template("ingredients.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True)