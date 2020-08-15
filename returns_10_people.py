from top_photo import best_photos
from data_base_VKinder.db import add_people
import json


def return_love(pr_key, data):
    #спиок для вывода и для добавления в BD
    people_list_print = []
    #список для сохранения в JSON
    poeple_list_return = []
    item = 0
    for person in data:
        link = f'https://vk.com/id{person["id"]}'
        # запуск функции модуля по отбору 3 фото
        photo = best_photos(person["id"])


        if photo == None:
            continue
        else:
            print_result = {'number': item, 'link': link, 'photo': photo, 'favorite': 0}
            print(print_result)
            # добавляеться primary key основного пользователя для дальнейшего добавления в DB
            result_DB = {'id': pr_key, 'link': link, 'photo': photo, 'favorite': 0}
            people_list_print.append(result_DB)
            result_return_JSON = {'link': link, 'photo': photo, 'favorite': 0}
            poeple_list_return.append(result_return_JSON)


            if item > 1 and (item % 10 == 0):
                query = input('If next press "n". Add to favorites press number. End press "q" ')
                add_database = people_list_print[item - 10:]


                if query == 'q':
                    # добавление каждые 10 человек в DB модуля db.py
                    add_people(add_database)
                    break
                elif query != ('q' and 'n'):
                    #добавление в избранное
                    try:
                        favorite = int(query)
                        poeple_list_return[favorite]['favorite'] = 1
                        people_list_print[favorite]['favorite'] = 1
                        add_people(add_database)
                        question = input('Favorite saved. If End press "q" ')
                        if question == 'q':
                            break
                    except:
                        print('Error input')
                        add_people(add_database)
                        continue
            item += 1
    with open('result_json\people_10.json', 'w',) as file:
        json.dump(poeple_list_return[item - 10:], file, ensure_ascii=False, indent=4)
    return poeple_list_return[item - 10:]



