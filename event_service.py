import shelve

db_name = 'library'
db_events_key = 'events'


def get_event_list():
    event_dict = {}
    db = shelve.open(db_name)
    if db_events_key in db:
        event_dict = db[db_events_key]
    db.close()
    return event_dict.values()


def save_event(event):
    event_dict = {}
    db = shelve.open(db_name)
    if db_events_key in db:
        event_dict = db[db_events_key]
    event_dict[event.id] = event
    db[db_events_key] = event_dict
    db.close()

def save_update_event(id, form):
    db = shelve.open(db_name, 'w')
    event_dict = db[db_events_key]

    db[db_events_key] = event_dict

    db.close()

def retrieve_event_from_id(id):
    db = shelve.open(db_name,'r')
    events_dict = db[db_events_key]
    db.close()
    return events_dict.get(id)


