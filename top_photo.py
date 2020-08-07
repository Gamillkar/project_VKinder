import requests
from operator import itemgetter
import re
token = '1f83abc61ca775b1ecdb057caf8243323dd7ae9853563d0cc81f93d17f970b1c1a0a03cca52cb8a459a61'

def best_photos(id):
    """Формирование топ-3 фото"""
    url = 'https://api.vk.com/method/photos.get'

    params = {'v': 5.61,
              'access_token': token,
              'owner_id': id,
              'album_id': 'profile',
              'extended': 1,
              'count': 100
    }

    photo_res = requests.get(url, params=params)
    data = (photo_res.json())['response']['items']
    list_photo_data = []
    for data_photo in data:
        # Т.к. репосты важны и редкие, то введен к ним коэффицент 20
        popularity = data_photo['likes']['count'] + data_photo['comments']['count'] + data_photo['reposts']['count'] * 20
        #подбор max качество фото
        pattern = re.compile('photo_(\d*)')
        result = pattern.findall(str(data_photo))
        format_photo = (sorted(result))[0]

        clear_data = data_photo[f'photo_{format_photo}'], popularity
        list_photo_data.append(clear_data)
    top = (sorted(list_photo_data, key=itemgetter(1), reverse=True))[:3]

    list_top_photo = []
    for photo in top:
        list_top_photo.append(photo[0])

    return list_top_photo


