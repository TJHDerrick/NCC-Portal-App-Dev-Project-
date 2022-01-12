from flask import Flask, render_template
from user_controller import user_controller

app = Flask(__name__)
app.register_blueprint(user_controller)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/kitExchange')
def kit_exchange():
    return render_template('kitExchange.html')


@app.route('/equipmentLoan')
def equipment_loan():
    return render_template('equipmentLoan.html')


@app.route('/facilityReservation')
def facility_reservation():
    return render_template('facilityReservation.html')


@app.route('/events')
def events():
    return render_template('events.html')


if __name__ == '__main__':
    app.run(port=5001)
