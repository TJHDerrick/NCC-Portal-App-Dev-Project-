import shelve

from flask import Blueprint, render_template, request, redirect, url_for
from event_forms import CreateEventForm
from event import Event
from event_service import get_event_list, save_event, save_update_event, retrieve_event_from_id

event_controller = Blueprint('event', __name__)


@event_controller.route('/retrieveEvents')
def retrieve_events():
    event_list = get_event_list()
    return render_template('retrieveEvent.html', count=len(event_list), event_list=event_list)


@event_controller.route('/createEvent', methods=['GET', 'POST'])
def create_event():
    create_event_form = CreateEventForm(request.form)
    if request.method == 'POST' and create_event_form.validate():
        title = create_event_form.title.data
        description = create_event_form.description.data
        start_date = create_event_form.start_date.data
        end_date = create_event_form.end_date.data
        time = create_event_form.time.data
        location = create_event_form.eventlocation.data
        visibility = create_event_form.visibility.data
        image = None
        sign_up_no = create_event_form.sign_up_no.data
        event = Event(title, description, start_date, end_date, time, location, visibility, image, sign_up_no)
        print(event)

        save_event(event)
        # return redirect('/retrieveUsers')
        return redirect(url_for('event.retrieve_events'))
    return render_template('createEvent.html', form=create_event_form)


@event_controller.route('/updateEvent/<id>/', methods=['GET', 'POST'])
def update_event(id):
    update_event_form = CreateEventForm(request.form)
    if request.method == 'POST' and update_event_form.validate():
        db = shelve.open('library', 'w')
        events_dict = db['events']

        event = events_dict.get(id)
        event.set_title(update_event_form.title.data)
        event.set_description(update_event_form.description.data)
        event.set_start_date(update_event_form.start_date.data)
        event.set_end_date(update_event_form.end_date.data)
        event.set_time(update_event_form.time.data)
        event.set_location(update_event_form.eventlocation.data)
        event.set_visibility(update_event_form.visibility.data)
        event.set_sign_up_no(update_event_form.sign_up_no.data)

        print(update_event_form.eventlocation.data)
        db['events'] = events_dict

        return redirect(url_for('event.retrieve_events'))
    else:
        event = retrieve_event_from_id(id)
        update_event_form.title.data = event.get_title()
        update_event_form.description.data = event.get_description()
        update_event_form.start_date.data = event.get_start_date()
        update_event_form.end_date.data = event.get_end_date()
        update_event_form.time.data = event.get_time()
        update_event_form.eventlocation.data = event.get_location()
        update_event_form.visibility.data = event.get_visibility()
        update_event_form.sign_up_no.data = event.get_sign_up_no()
        return render_template('updateEvent.html', form=update_event_form)


@event_controller.route('/deleteEvent/<id>', methods=['POST'])
def delete_event(id):
    db = shelve.open('library', 'w')
    events_dict = db['events']
    event = events_dict.pop(id)
    db['events'] = events_dict
    db.close()
    return redirect(url_for('event.retrieve_events'))
