from flask import render_template, request
from app import app
from app.models.events_list import *

@app.route('/')
def index():   

    return render_template('index.html', title='Home', events=events)


@app.route('/add-event', methods=['POST'])
def add_event():
    event_title = request.form[ 'title']
    event_date = request.form['date']
    event_number_of_guests = request.form['number_of_guests']
    event_room_location = request.form['room_location']
    event_desc = request.form['description']
    event_recurring = request.form['recurring']

    new_event = Event(event_title, event_date, event_number_of_guests, event_room_location, event_desc, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

