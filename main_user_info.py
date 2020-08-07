import requests
from datetime import datetime
token = '1f83abc61ca775b1ecdb057caf8243323dd7ae9853563d0cc81f93d17f970b1c1a0a03cca52cb8a459a61'

def main_user_info(id):
    """Получение информации об основном пользователе"""

    url = 'https://api.vk.com/method/users.get'
    params = {'v': 5.61,
              'access_token': token,
              'user_ids': id,
              'fields': 'sex,city,bdate,country'
              }
    data_us = (requests.get(url, params=params)).json()['response'][0]

    main_user = [data_us['bdate'], data_us['city']['id'], data_us['country']['id'], data_us['sex']]

    # вычесление возраста
    today = datetime.today()
    time_main = main_user[0]
    born = datetime.strptime(time_main, "%d.%m.%Y")
    range_time = today - born
    years = int(range_time.days / 365)
    main_user.append(years)

    return main_user #возвращает год рождения, id города, id страны, пол, возраст







