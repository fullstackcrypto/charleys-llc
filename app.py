from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure the SMTP server settings for Namecheap Private Email
app.config['MAIL_SERVER'] = 'mail.privateemail.com'  # Namecheap's Private Email server
app.config['MAIL_PORT'] = 587  # Use port 587 for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'charley@charleysllc.com'  # Your Namecheap email address
app.config['MAIL_PASSWORD'] = 'Matrix4228!'  # Replace with the email password

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Log the contact form submission
        print(f"New contact form submission from {name} ({email}): {message}")

        # Send email notification
        msg = Message('New Contact Form Submission',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"""
        You have received a new contact form submission:

        Name: {name}
        Email: {email}
        Message: {message}
        """
        mail.send(msg)

        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
