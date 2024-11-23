from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')
        
        # Here you would typically add code to:
        # 1. Send an email notification
        # 2. Store the contact request in a database
        # For now, we'll just show a success message
        
        flash(f'Thank you {name}! We will contact you soon about your {service} request.')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Add error handlers for better user experience
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)