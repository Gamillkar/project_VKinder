from top_photo import best_photos

def return_love(data):
    people_list = []
    for item, person in enumerate(data):
        link = f'https://vk.com/id{person["id"]}, '
        # запуск функции модуля по отбору 3 фото
        photo = best_photos(person["id"])
        if photo == None:
            continue
        else:
            result = f'{link} {photo}'
            people_list.append(result)
            print(result)
            print(item)
        if item > 1 and (item % 10 == 0):
            query = input('if next press "n". If complete press "q" ')
            if query == 'q':
                break
    return people_list



