from Product import *
from Store import *

if __name__ == "__main__":

    store_inst = Store('cool stuff')
    prduct_id = 1
    prduct1 = Product('Product1', 10, 'cat1', prduct_id)
    prduct_id += 1
    prduct2 = Product('Product2', 20, 'cat2',prduct_id)
    prduct_id += 1
    prduct3 = Product('Product3', 30, 'cat2', prduct_id)
    
    store_inst.add_product(prduct1)
    store_inst.add_product(prduct2)
    store_inst.add_product(prduct3)
    
    store_inst.print_products()
    print('-------')
    store_inst.inflation(0.2)
    store_inst.print_products()
    print('-------')
    store_inst.sell_product(1)
    print('-------')

    store_inst.set_clearance('cat2', 0.2)
    store_inst.print_products()

