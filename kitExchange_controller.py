import shelve

from flask import Blueprint, render_template, request, redirect, url_for
from kitExchange_forms import CreateCreationForm
from kitExchangeCreation import Creation
from kitExchange_service import get_creation_list, save_creation, save_update_creation, retrieve_creation_from_id

kitExchange_controller = Blueprint('creation', __name__)


@kitExchange_controller.route('/kitExchange')
def retrieve_creation():
    creation_list = get_creation_list()
    return render_template('kitExchange.html', count=len(creation_list), creation_list=creation_list)


@kitExchange_controller.route('/kitExchange_Admin')
def retrieve_creation_admin():
    creation_list = get_creation_list()
    return render_template('kitExchange_Admin.html', count=len(creation_list), creation_list=creation_list)


@kitExchange_controller.route('/kitExchangeCreation', methods=['GET', 'POST'])
def create_creation():
    create_creation_form = CreateCreationForm(request.form)
    if request.method == 'POST' and create_creation_form.validate():
        name = create_creation_form.name.data
        description = create_creation_form.description.data
        sizes = create_creation_form.sizes.data
        location = create_creation_form.location.data
        creation = Creation(name, description, sizes, location)
        print(creation)

        save_creation(creation)
        # return redirect('/retrieveUsers')
        return redirect(url_for('creation.retrieve_creation'))
    return render_template('kitExchangeCreation.html', form=create_creation_form)


@kitExchange_controller.route('/updatekitExchange/<id>/', methods=['GET', 'POST'])
def update_kit(id):
    update_creation_form = CreateCreationForm(request.form)
    if request.method == 'POST' and update_creation_form.validate():
        db = shelve.open('library', 'w')
        creation_dict = db['creation']

        creation = creation_dict.get(id)
        creation.set_name(update_creation_form.name.data)
        creation.set_description(update_creation_form.description.data)
        creation.set_sizes(update_creation_form.sizes.data)
        creation.set_location(update_creation_form.location.data)

        print(update_creation_form.location.data)
        db['creation'] = creation_dict

        return redirect(url_for('creation.retrieve_creation_admin'))
    else:
        creation = retrieve_creation_from_id(id)
        update_creation_form.name.data = creation.get_name()
        update_creation_form.description.data = creation.get_description()
        update_creation_form.sizes.data = creation.get_sizes()
        update_creation_form.location.data = creation.get_location()
        return render_template('updatekitExchange.html', form=update_creation_form)


@kitExchange_controller.route('/deleteCreation/<id>', methods=['POST'])
def delete_creation(id):
    db = shelve.open('library', 'w')
    creation_dict = db['creation']
    creation = creation_dict.pop(id)
    db['creation'] = creation_dict
    db.close()
    return redirect(url_for('creation.retrieve_creation_admin'))
