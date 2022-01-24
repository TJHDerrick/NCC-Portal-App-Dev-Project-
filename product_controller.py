import shelve

from flask import Blueprint, render_template, request, redirect, url_for
from product_form import ProductCreationForm
from productCreation import Product_Creation
from kitExchange_service import get_creation_list, save_creation, save_update_creation, retrieve_creation_from_id

product_controller = Blueprint('product_creation', __name__)


@product_controller.route('/product')
def retrieve_product_creation():
    creation_list = get_creation_list()
    return render_template('product.html', count=len(creation_list), creation_list=creation_list)


@product_controller.route('/product_Admin')
def retrieve_product_creation_admin():
    creation_list = get_creation_list()
    return render_template('product_Admin.html', count=len(creation_list), creation_list=creation_list)


@product_controller.route('/create_Product', methods=['GET', 'POST'])
def create_product():
    create_product_creation_form = ProductCreationForm(request.form)
    if request.method == 'POST' and create_product_creation_form.validate():
        name = create_product_creation_form.name.data
        description = create_product_creation_form.description.data
        sizes = create_product_creation_form.sizes.data
        location = create_product_creation_form.location.data
        creation = Product_Creation(name, description, sizes, location)
        print(creation)

        save_creation(creation)
        # return redirect('/retrieveUsers')
        return redirect(url_for('product_creation.retrieve_product_creation'))
    return render_template('create_Product.html', form=create_product_creation_form)


@product_controller.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_creation_form = ProductCreationForm(request.form)
    if request.method == 'POST' and update_product_creation_form.validate():
        db = shelve.open('library', 'w')
        creation_dict = db['creation']

        creation = creation_dict.get(id)
        creation.set_name(update_product_creation_form.name.data)
        creation.set_description(update_product_creation_form.description.data)
        creation.set_sizes(update_product_creation_form.sizes.data)
        creation.set_location(update_product_creation_form.location.data)

        print(update_product_creation_form.location.data)
        db['creation'] = creation_dict

        return redirect(url_for('Product_Creation.retrieve_product_creation_admin'))
    else:
        creation = retrieve_creation_from_id(id)
        update_product_creation_form.name.data = creation.get_name()
        update_product_creation_form.description.data = creation.get_description()
        update_product_creation_form.sizes.data = creation.get_sizes()
        update_product_creation_form.location.data = creation.get_location()
        return render_template('updateProduct.html', form=update_product_creation_form)


@product_controller.route('/deleteCreation/<int:id>', methods=['POST'])
def delete_product(id):
    db = shelve.open('library', 'w')
    creation_dict = db['creation']
    creation = creation_dict.pop(id)
    db['creation'] = creation_dict
    db.close()
    return redirect(url_for('creation.retrieve_creation_admin'))