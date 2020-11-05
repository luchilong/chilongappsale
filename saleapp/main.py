from urllib import request

from flask import render_template
from saleapp import app, utils


@app.route('/')
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)


@app.route('/products')
def product_list():
    cate_id = request.get('category_id')
    products = utils.read_data(cate_id=cate_id)
    return render_template('product-list.html',
                           products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)
    return render_template('product-detail.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
