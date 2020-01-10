def view_list(products):
    for i in range(len(products)):
        print (f'{i} -- {products[i]}')

def add_products(products):
    list_products = []
    new_products = products.split(',')
    for new in new_products:
        list_products.append(new)
    return list_products

def delete_products(new_products):
    select = input('¿Que producto ya compraste? (Selecciona el número del producto): ')
    del new_products[int(select)]
    return new_products


if __name__ == '__main__':
    products = input('Que productos te gustaría agregar a tu lista de compras \n[Separalos por una coma (,)]:')
    new_products = add_products(products)
    view_list(new_products)
    delete = delete_products(new_products)
    while len(delete) > 0:
        view_list(delete)
        new = delete_products(delete)
    else:
        print('¡Terminaste tu lista de compras!')