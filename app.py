from flask import Flask, render_template, request, redirect
import os

app = Flask(**name**, template_folder=‘templates’, static_folder=‘static’)

@app.route(’/’)
def index():
return render_template(‘index.html’)

@app.route(’/services’)
def services():
return render_template(‘services.html’)

@app.route(’/pricing’)
def pricing():
return render_template(‘pricing.html’)

@app.route(’/booking’)
def booking():
return render_template(‘booking.html’)

@app.route(’/contact’)
def contact():
return render_template(‘contact.html’)

@app.route(’/thanks’)
def thanks():
return render_template(‘thanks.html’)

if **name** == ‘**main**’:
port = int(os.environ.get(“PORT”, 5000))
app.run(debug=True, host=‘0.0.0.0’, port=port)