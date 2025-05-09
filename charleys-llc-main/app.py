from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Contact page route
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Services page route
@app.route("/services")
def services():
    return render_template("services.html")

# Thank You page route
@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)