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


@signup_controller.route('/deleteSignUp/<id>', methods=['POST'])
def delete_signup(id):
    delete_sign_up(id)
    return redirect(url_for('signup.retrieve_signups'))
