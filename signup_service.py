import shelve

db_name = 'library'
db_signups_key = 'signup'


def get_signup_list():
    signup_dict = {}
    db = shelve.open(db_name)
    if db_signups_key in db:
        signup_dict = db[db_signups_key]
    db.close()
    return signup_dict.values()


def save_signup(signup):
    signup_dict = {}
    db = shelve.open(db_name)
    if db_signups_key in db:
        signup_dict = db[db_signups_key]
    signup_dict[signup.id] = signup
    db[db_signups_key] = signup_dict
    db.close()

# # def save_update_event(id, form):
# #     db = shelve.open(db_name, 'w')
# #     event_dict = db[db_events_key]
# #
# #     db[db_events_key] = event_dict
# #
# #     db.close()
#
# def retrieve_event_from_id(id):
#     db = shelve.open(db_name,'r')
#     events_dict = db[db_events_key]
#     db.close()
#     return events_dict.get(id)

def delete_sign_up(id):
    db = shelve.open('library', 'w')
    signup_dict = db['signup']
    signup_dict.pop(id)
    db['signup'] = signup_dict
    db.close()
