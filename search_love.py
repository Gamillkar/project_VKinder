import requests
from tokens import token


def query_people(data, age_1=None, age_2=None):
    """Поиск людей. Формирование списка людей с id и топ-3 фото"""
    search_love = 'https://api.vk.com/method/users.search'

    #определение противоположного пола
    if data[4] == 2:
        research_gender = 1
    else:
        research_gender = 2

    #определения диапозона возраста, если пользователь не указал
    if research_gender == 1 and (age_1 and age_2 == None):
        age_from = 18
        age_to = data[5] + 5 #возраст male + 5 лет
    elif research_gender == 2 and (age_1 and age_2 == None):
        age_from = data[5] - 3
        age_to = data[5] + 8
    #переопределение age если указан диапазон
    else:
        age_from = age_1
        age_to = age_2
    params = {'v': 5.61,
              'access_token': token,
              'q':'',
              'sort':'0',
              'count': 1000,
              'city':data[2],
              'country':data[3],
              'sex':research_gender,
              'status': 1,
              'age_from': age_from,
              'age_to': age_to,
              'has_photo': 1
    }
    love_res = requests.get(search_love, params=params)
    data = love_res.json()
    data = data['response']['items']
    return data


