from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Route for Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for Membership page
@app.route('/membership')
def membership():
    return render_template('membership.html')

# Route for Contact Us page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Logic to handle contact form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Logic to save or send email
        return redirect(url_for('home'))
    return render_template('contact.html')

# Route for Sign In page
@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
