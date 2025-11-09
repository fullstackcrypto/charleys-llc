from app import db
from datetime import datetime

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float)
    duration = db.Column(db.Integer)  # in minutes
    category = db.Column(db.String(50))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    client_name = db.Column(db.String(100))
    client_email = db.Column(db.String(120))
    scheduled_time = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)