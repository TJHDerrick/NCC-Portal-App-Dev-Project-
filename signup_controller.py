import shelve

from flask import Blueprint, render_template, request, redirect, url_for, flash
from event_forms import SignUpForm
from event import SignUp
from signup_service import get_signup_list, save_signup, delete_sign_up

signup_controller = Blueprint('signup', __name__)
# flash("All OK")
# flash("All OK", 'success')
# flash("All Normal", 'info')
# flash("Not So OK", 'error')
# flash("So So", 'warning')


@signup_controller.route('/retrieveSignUp')
def retrieve_signups():
    signup_list = get_signup_list()
    return render_template('retrieveSignUp.html', count=len(signup_list), signup_list=signup_list)


@signup_controller.route('/SignUp', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpForm(request.form)
    if request.method == 'POST' and sign_up_form.validate():
        eventname = sign_up_form.eventname.data
        name = sign_up_form.name.data
        nric = sign_up_form.nric.data
        school = sign_up_form.school.data
        email = sign_up_form.email.data
        awareness = sign_up_form.awareness.data
        notification = sign_up_form.notification.data
        signup = SignUp(eventname, name, nric, school, email, awareness, notification)
        print(signup)

        save_signup(signup)
        # return redirect('/retrieveUsers')
        flash("Sign up successful", 'success')
        return redirect(url_for('signup.retrieve_signups'))
    return render_template('SignUp.html', form=sign_up_form)


# @event_controller.route('/updateEvent/<id>/', methods=['GET', 'POST'])
# def update_event(id):
#     update_event_form = CreateEventForm(request.form)
#     if request.method == 'POST' and update_event_form.validate():
#         db = shelve.open('library', 'w')
#         events_dict = db['events']
#
#         event = events_dict.get(id)
#         event.set_title(update_event_form.title.data)
#         event.set_description(update_event_form.description.data)
#         event.set_start_date(update_event_form.start_date.data)
#         event.set_end_date(update_event_form.end_date.data)
#         event.set_time(update_event_form.time.data)
#         event.set_location(update_event_form.eventlocation.data)
#         event.set_visibility(update_event_form.visibility.data)
#         event.set_sign_up_no(update_event_form.sign_up_no.data)
#
#         print(update_event_form.eventlocation.data)
#         db['events'] = events_dict
#
#         return redirect(url_for('event.retrieve_events'))
#     else:
#         event = retrieve_event_from_id(id)
#         update_event_form.title.data = event.get_title()
#         update_event_form.description.data = event.get_description()
#         update_event_form.start_date.data = event.get_start_date()
#         update_event_form.end_date.data = event.get_end_date()
#         update_event_form.time.data = event.get_time()
#         update_event_form.eventlocation.data = event.get_location()
#         update_event_form.visibility.data = event.get_visibility()
#         update_event_form.sign_up_no.data = event.get_sign_up_no()
#         return render_template('updateEvent.html', form=update_event_form)


@signup_controller.route('/deleteSignUp/<id>', methods=['POST'])
def delete_signup(id):
    delete_sign_up(id)
    return redirect(url_for('signup.retrieve_signups'))
