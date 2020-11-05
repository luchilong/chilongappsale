import json


def read_data(path='data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_product_by_id(product_id):
    products = read_data('data/products.json')
    for p in products:
        if p['id'] == product_id:
            return p


def read_products(cate_id=None):
    products = read_data(path='data/products.json')

    if cate_id:
        cate_id = int(cate_id)
        products = [p for p in products\
                    if p['category_id'] == cate_id]

    return products