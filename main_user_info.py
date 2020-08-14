import requests
from datetime import datetime
from tokens import token


def main_user_info(id):
    """Получение информации об основном пользователе"""

    url = 'https://api.vk.com/method/users.get'
    params = {'v': 5.61,
              'access_token': token,
              'user_ids': id,
              'fields': 'sex,city,bdate,country'
              }
    data_us = (requests.get(url, params=params)).json()['response'][0]
    main_user = [data_us['id'], data_us['bdate'], data_us['city']['id'], data_us['country']['id'], data_us['sex']]

    # вычесление возраста
    today = datetime.today()
    time_main = main_user[1]
    born = datetime.strptime(time_main, "%d.%m.%Y")
    range_time = today - born
    years = int(range_time.days / 365)
    main_user.append(years)

    return main_user #возвращает год рождения, id города, id страны, пол, возраст






