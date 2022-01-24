import shelve

db_name = 'library'
db_creation_key = 'product_creation'


def get_creation_list():
    creation_dict = {}
    db = shelve.open(db_name)
    if db_creation_key in db:
        creation_dict = db[db_creation_key]
    db.close()
    return creation_dict.values()


def save_creation(creation):
    creation_dict = {}
    db = shelve.open(db_name)
    if db_creation_key in db:
        creation_dict = db[db_creation_key]
    creation_dict[creation.id] = creation
    db[db_creation_key] = creation_dict
    db.close()

def save_update_creation(id, form):
    db = shelve.open(db_name, 'w')
    creation_dict = db[db_creation_key]

    db[db_creation_key] = creation_dict

    db.close()

def retrieve_creation_from_id(id):
    db = shelve.open(db_name, 'r')
    creation_dict = db[db_creation_key]
    db.close()
    return creation_dict.get(id)