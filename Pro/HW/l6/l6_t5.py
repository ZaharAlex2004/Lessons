import xml.etree.ElementTree as ET


def product(files):
    """
    Выводим продукты.
    :param files:
    :return:
    """
    tree = ET.parse(files)
    root = tree.getroot()

    for product in root.findall('product'):
        name = product.find('name').text
        price = product.find('price').text
        quantity = product.find('quantity').text
        print(f'{name}, Вартість: {price} грн. Кількість {quantity}')


def new_quant(xml_p, product_name, new_q):
    """
    Добавляем количество.
    :param xml_p:
    :param product_name:
    :param new_q:
    :return:
    """
    tree = ET.parse(xml_p)
    root = tree.getroot()

    product_found = False
    for product in root.findall('product'):
        name = product.find('name').text
        if name == product_name:
            product.find('quantity').text = str(new_q)
            print(f'\nКількість продукта "{name}" оновлено на {new_q}.')
            product_found = True
            break
    if not product_found:
        print(f'Продукт "{product_name}" не знайдений.')

    tree.write(xml_p, encoding='utf-8')


pr = 'product.xml'

product(pr)

update_prod = input('\nВведіть назву продукта: ')
new_col = input('Введіть нову кількість: ')
new_quant(pr, update_prod, new_col)

print('\nОновлені дані.')
product(pr)
