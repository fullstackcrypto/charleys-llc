from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Security and Configuration Settings
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Email Configuration
app.config.update(
    MAIL_SERVER=os.environ.get('MAIL_SERVER', 'mail.privateemail.com'),
    MAIL_PORT=int(os.environ.get('MAIL_PORT', 587)),
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME', 'charley@charleysllc.com'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER', 'charley@charleysllc.com')
)

# File Upload Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mail = Mail(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            service = request.form.get('service')
            message = request.form.get('message')
            
            # Handle file uploads
            attachments = []
            if 'files' in request.files:
                files = request.files.getlist('files')
                for file in files:
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file.save(filepath)
                        attachments.append(filepath)

            # Create email message
            msg = Message(
                subject=f'New Contact Form Submission - {service}',
                recipients=[app.config['MAIL_USERNAME']],
                body=f"""
New contact form submission from your website:

Name: {name}
Email: {email}
Phone: {phone}
Service Requested: {service}

Message:
{message}
                """
            )

            # Add attachments to email
            for attachment in attachments:
                with open(attachment, 'rb') as f:
                    msg.attach(
                        filename=os.path.basename(attachment),
                        content_type='application/octet-stream',
                        data=f.read()
                    )

            # Send auto-reply to customer
            auto_reply = Message(
                subject='Thank you for contacting CHARLEY\'S LLC',
                recipients=[email],
                body=f"""
Dear {name},

Thank you for contacting CHARLEY'S LLC. We have received your message regarding {service}.

We will review your request and get back to you within 24 hours.

Best regards,
CHARLEY'S LLC Team
                """
            )

            # Send emails
            mail.send(msg)
            mail.send(auto_reply)
            flash('Thank you! Your message has been sent successfully. We will contact you soon.')

        except Exception as e:
            print(f"Error processing contact form: {e}")
            flash('There was an error sending your message. Please try calling us directly.')

        finally:
            # Clean up uploaded files
            for attachment in attachments:
                try:
                    os.remove(attachment)
                except Exception as e:
                    print(f"Error removing file {attachment}: {e}")

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(413)
def too_large(e):
    flash('File is too large. Maximum size is 16MB.')
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_ENV') == 'development')