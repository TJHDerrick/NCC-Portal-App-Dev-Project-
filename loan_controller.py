import shelve

from flask import Blueprint, render_template, request, redirect, url_for
from loan_forms import CreateLoanForm, UpdateLoanForm
from loan import Loan
from loan_service import get_loan_list, save_loan, save_update_loan, retrieve_loan_from_id

loan_controller = Blueprint('loan', __name__)


@loan_controller.route('/retrieveLoan')
def retrieve_loan():
    loan_list = get_loan_list()
    return render_template('retrieveLoan.html', count=len(loan_list), loan_list=loan_list)

@loan_controller.route('/successLoan')
def success_loan():
        create_loan_form = CreateLoanForm(request.form)
        if request.method == 'POST' and create_loan_form.validate():
            email = create_loan_form.email.data
            number = create_loan_form.number.data
            date = create_loan_form.date.data
            choice = create_loan_form.choice.data
        return render_template('successLoan.html',)

@loan_controller.route('/createLoan', methods=['GET', 'POST'])
def create_loan():
    create_loan_form = CreateLoanForm(request.form)
    if request.method == 'POST' and create_loan_form.validate():
        email = create_loan_form.email.data
        number = create_loan_form.number.data
        date = create_loan_form.date.data
        choice = create_loan_form.choice.data

        loan = Loan(email, number, date, choice)
        print(loan)

        save_loan(loan)
        # return redirect('/retrieveUsers')
        return redirect(url_for('loan.success_loan'))
    return render_template('createLoan.html', form=create_loan_form)


@loan_controller.route('/updateloan/<id>/', methods=['GET', 'POST'])
def update_loan(id):
    loan = retrieve_loan_from_id(id)
    update_loan_form = UpdateLoanForm(request.form)

    if request.method == 'GET':
        update_loan_form.email.data = loan.get_email()
        update_loan_form.number.data = loan.get_number()
        update_loan_form.date.data = loan.get_date()
        update_loan_form.choice.data = loan.get_choice()
        return render_template('updateLoan.html', form=update_loan_form)

    if request.method == 'POST':
        if update_loan_form.validate():
            db = shelve.open('library', 'w')
            loan_dict = db['loan']

            loan = loan_dict.get(id)
            loan.set_email(update_loan_form.email.data)
            loan.set_number(update_loan_form.number.data)
            loan.set_date(update_loan_form.date.data)
            loan.set_choice(update_loan_form.choice.data)

            db['loan'] = loan_dict

            return redirect(url_for('loan.retrieve_loan'))
        else:

            return render_template('updateLoan.html', form=update_loan_form)


@loan_controller.route('/deleteloan/<id>', methods=['POST'])
def delete_loan(id):
    db = shelve.open('library', 'w')
    loan_dict = db['loan']
    loan = loan_dict.pop(id)
    db['loan'] = loan_dict
    db.close()
    return redirect(url_for('loan.retrieve_loan'))
