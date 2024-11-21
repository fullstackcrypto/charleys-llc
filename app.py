from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# Configuration for the uploads folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Serve sign-in page
@app.route('/signin.html')
def signin():
    return render_template('signin.html')

# Handle file uploads from contact form
@app.route('/contact', methods=['POST'])
def contact():
    if 'file' not in request.files:
        return 'No file part in the form', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
