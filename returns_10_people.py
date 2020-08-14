from top_photo import best_photos
from data_base_VKinder.db import add_people
import json


def return_love(pr_key, data):
    people_list = []
    item = 0
    for person in data:
        link = f'https://vk.com/id{person["id"]}'
        # запуск функции модуля по отбору 3 фото
        photo = best_photos(person["id"])


        if photo == None:
            continue
        else:
            if item > 1 and (item % 10 == 0):
                query = input('If next press "n". Add to favorites press number. End press "q" ')
                add_database = people_list[item - 10:]

                if query == 'q':
                    # добавление каждые 10 человек в DB
                    add_people(add_database)
                    break
                elif query != ('q' and 'n'):
                    #добавление в избранное
                    try:
                        favorite = int(query)
                        people_list[favorite]['favorite'] = 1
                        add_people(add_database)
                    except:
                        print('Error input')
                        add_people(add_database)
            print_result = {'number': item, 'link':link, 'photo':photo, 'favorite':0}
            #добавляеться primary key основного пользователя для дальнейшего добавления в DB
            result = {'id': pr_key, 'link':link, 'photo':photo, 'favorite':0}
            people_list.append(result)
            print(print_result)
            item += 1

    with open('result_json\people_10.json', 'w',) as file:
        json.dump(people_list[item - 10:], file, ensure_ascii=False, indent=4)
    return people_list[item - 10:]



