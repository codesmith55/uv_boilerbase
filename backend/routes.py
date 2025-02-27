from flask import Blueprint, request, jsonify
from models import db, Event
from apscheduler.schedulers.background import BackgroundScheduler

bp = Blueprint('main', __name__)
scheduler = BackgroundScheduler()
scheduler.start()

def add_scheduled_job(addFunc, type='interval', interval=2):
    print(f"Adding scheduled job with type {type} and interval {interval} seconds")  # Debugging statement
    scheduler.add_job(addFunc, 'interval', seconds=interval)

@bp.route('/events', methods=['POST'])
def add_event():
    data = request.json
    new_event = Event(location=data['location'], type=data['type'], typeDetails=data['typeDetails'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added'}), 201

@bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': event.id, 'location': event.location, 'type': event.type, 'typeDetails': event.typeDetails} for event in events])

@bp.route('/start-monitoring', methods=['POST'])
def start_monitoring():
    interval = 2  # Default interval is 5 seconds
    type='temp'
    print(f"Adding scheduled job with type {type} and interval {interval} seconds")  # Debugging statement
    scheduler.add_job(start_monitoring, 'interval', seconds=interval)
    return jsonify({'message': 'Monitoring started'}), 200

