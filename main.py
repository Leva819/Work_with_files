def cook_book(file):
    with open(file, 'r', encoding='utf-8') as file:
        file.seek(0)
        cook_book = {}
        for line in file:
            ingredients = []
            name_of_dish = line.strip()
            amount_of_ingredients = int(file.readline().strip())
            for i in range(amount_of_ingredients):
                name, count, measure = file.readline().strip().split('|')
                ingredients.append(
                    {'ingredient_name': name.strip(), 'quantity': int(count), 'measure': measure.strip()})
            file.readline()
            cook_book[name_of_dish] = ingredients
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    for i in cook_book('C:\Work\RECEPIE_FAIL\RECEPIE.txt'):
        shop_list = {}
        for dish in dishes:
            for ingredient in cook_book('C:\Work\RECEPIE_FAIL\RECEPIE.txt')[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count

                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

list = []
dict_ = {}
with open('C:\Work\RECEPIE_FAIL\Files\File_1.txt', 'r', encoding='utf-8') as f_1:
    text_1 = f_1.readlines()
    count_1 = len(text_1)
    dict_[count_1] = text_1
    list.append(count_1)
    f_1.seek(0)
with open('C:\Work\RECEPIE_FAIL\Files\File_2.txt', 'r', encoding='utf-8') as f_2:
    text_2 = f_2.readlines()
    count_2 = len(text_2)
    dict_[count_2] = text_2
    list.append(count_2)
    f_2.seek(0)
with open('C:\Work\RECEPIE_FAIL\Files\File_3.txt', 'r', encoding='utf-8') as f_3:
    text_3 = f_3.readlines()
    count_3 = len(text_3)
    dict_[count_3] = text_3
    list.append(count_3)
    f_3.seek(0)
list.sort()
for i in list:
    for key, value in dict_.items():
        if i == key:
                with open('C:\Work\RECEPIE_FAIL\Files\Common.txt', 'a', encoding='utf-8') as file:
                    if key == count_3:
                        file.write('\n')
                        file.write('\n')
                        file.write('File_3')
                        file.write('\n')
                    elif key == count_2:
                        file.write('\n')
                        file.write('\n')
                        file.write('File_2')
                        file.write('\n')
                    else:
                        file.write('\n')
                        file.write('\n')
                        file.write('File_3')
                        file.write('\n')
                    file.write('\n')
                    file.write(str(i))
                    file.write('\n')
                for string in value:
                    with open('C:\Work\RECEPIE_FAIL\Files\Common.txt', 'a', encoding='utf-8') as file:
                        file.write(string)



