import shelve

db_name = 'library'
db_loans_key = 'loan'


def get_loan_list():
    loan_dict = {}
    db = shelve.open(db_name)
    if db_loans_key in db:
        loan_dict = db[db_loans_key]
    db.close()
    return loan_dict.values()


def save_loan(loan):
    loan_dict = {}
    db = shelve.open(db_name)
    if db_loans_key in db:
        loan_dict = db[db_loans_key]
    loan_dict[loan.id] = loan
    db[db_loans_key] = loan_dict
    db.close()

def save_update_loan(id, form):
    db = shelve.open(db_name, 'w')
    loan_dict = db[db_loans_key]

    db[db_loans_key] = loan_dict

    db.close()

def retrieve_loan_from_id(id):
    db = shelve.open(db_name,'r')
    loans_dict = db[db_loans_key]
    db.close()
    return loans_dict.get(id)

