
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_toastr import Toastr
# from user_controller import user_controller
from event_controller import event_controller
from signup_controller import signup_controller
from Forms import CreateUserForm, UserSignUp, CreateCustomerForm, Login
import shelve, Person, Customer
from kitExchange_controller import kitExchange_controller
from product_controller import product_controller

app = Flask(__name__)
app.secret_key = 'Hello world'
toastr = Toastr(app)
toastr.init_app(app)
# app.register_blueprint(user_controller)
app.register_blueprint(event_controller)
app.register_blueprint(signup_controller)

app.register_blueprint(kitExchange_controller)
app.register_blueprint(product_controller)


@app.route('/')
def home():
    flash("Don't tell anyone")
    return render_template('home.html')


@app.route('/kitExchange_Admin')
def kit_exchange_admin():
    return render_template('kitExchange_Admin.html')


@app.route('/product_Admin')
def product_exchange_admin():
    return render_template('product_Admin.html')


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


@app.route('/testhomestaff')
def home_staff():
    return render_template('testhomestaff.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = Person.Person(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.email.data,create_user_form.membership.data)
        users_dict[user.get_person_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/retrieveUsers')
def retrieve_users():
    # users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        # users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_email(update_user_form.email.data)
        user.set_membership(update_user_form.membership.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        # users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.email.data = user.get_email()
        update_user_form.membership.data = user.get_membership()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    # users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))


@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_cust_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_cust_form.validate():
        user_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            user_dict = db['Customer']
        except:
            print("Error in retrieving Users from customer.db.")

        user = Person.Person(create_cust_form.first_name.data, create_cust_form.last_name.data, create_cust_form.gender.data, create_cust_form.email.data,create_cust_form.membership.data)
        user_dict[user.get_person_id()] = user
        db['Customer'] = user_dict

        db.close()

        return redirect(url_for('retrieve_customer'))
    return render_template('createCustomer.html', form=create_cust_form)


@app.route('/retrieve_Customer')
def retrieve_customer():
    user_dict = {}
    db = shelve.open('customer.db', 'r')
    user_dict = db['Customer']
    db.close()

    user_list = []
    for key in user_dict:
        user = user_dict.get(key)
        user_list.append(user)

    return render_template('retrieve_Customer.html', count=len(user_list), users_list=user_list)


@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    user_dict = {}
    db = shelve.open('customer.db', 'w')
    user_dict = db['Customer']

    user_dict.pop(id)

    db['Customer'] = user_dict
    db.close()

    return redirect(url_for('retrieve_customer'))


@app.route('/user_Signup', methods=['GET', 'POST'])
def join_now():
    user_sign_up = UserSignUp(request.form)
    if request.method == 'POST' and user_sign_up.validate():
        user_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            user_dict = db['Customer']
        except:
            print("Error in retrieving Users from customer.db.")

        user = Customer.Customer(user_sign_up.first_name.data, user_sign_up.last_name.data, user_sign_up.gender.data,
                                 user_sign_up.email.data, user_sign_up.membership.data, user_sign_up.password.data,
                                 user_sign_up.confirmpassword.data)
        user_dict[user.get_person_id()] = user
        db['Customer'] = user_dict

        db.close()

        flash("Sign Up Successful!")

        return redirect(url_for('home'))

    return render_template('user_Signup.html', form=user_sign_up)


@app.route('/UserLogin', methods=['GET', 'POST'])
def login():
    user_login = Login(request.form)
    if request.method == 'POST' and user_login.validate():
        db = shelve.open('customer.db', 'r')
        user_dict = db['Customer']

        email_input = user_login.email.data
        password_input = user_login.password.data

        for key in user_dict:
            emailinshelve = user_dict[key].get_email()
            if email_input == emailinshelve:
                email_key = user_dict[key]
                validemail = True
                print("Registered Email & Inputted Email: ", emailinshelve, email_input)

                if validemail == True:
                    passwordinshelve = user_dict[key].get_password
                    if password_input == passwordinshelve():
                        flash("Success")

                        return redirect(url_for('home'))

        else:
            flash("Unsuccessful, check your email and password")
        db.close()

    return render_template('userLogin.html', form=user_login)


# @app.route('/createEvent')
# def create_event():
#     return render_template('createEvent.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
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

