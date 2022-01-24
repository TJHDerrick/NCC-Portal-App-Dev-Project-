from flask import Flask, render_template, flash
from flask_toastr import Toastr
from user_controller import user_controller
from event_controller import event_controller
from signup_controller import signup_controller
from loan_controller import loan_controller
from kitExchange_controller import kitExchange_controller


app = Flask(__name__)
app.secret_key = 'Hello world'
toastr = Toastr(app)
toastr.init_app(app)
app.register_blueprint(user_controller)
app.register_blueprint(event_controller)
app.register_blueprint(signup_controller)
app.register_blueprint(kitExchange_controller)
app.register_blueprint(loan_controller)

@app.route('/')
def home():
    flash("Welcome to NCC Portal")
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/kitExchange')
def kit_exchange():
    return render_template('kitExchange.html')


@app.route('/kitExchange_Admin')
def kit_exchange_admin():
    return render_template('kitExchange_Admin.html')


@app.route('/events')
def events():
    return render_template('events.html')


# @app.route('/createEvent')
# def create_event():
#     return render_template('createEvent.html')


if __name__ == '__main__':
    app.run(port=5002, debug=True)
