my_list = []
my_dict = {}

number_of_products = int(input('Enter number of products:'))
dict_num = 1

while dict_num <= number_of_products:
    my_dict = dict({'name': input('enter product name:'), 'price': input('enter product price:'),
                    'number': input('enter number of product:'), 'unit of measure': input('enter unit of measure:')})
    my_list.append((dict_num, my_dict))
    dict_num += 1
print(my_list)

# TODO завершить разработку словаря product_analytics
ct_analytics = {}
product_analytics.update(my_dict)
print(product_analytics)




