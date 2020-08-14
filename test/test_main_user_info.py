import unittest
from main_user_info import main_user_info as main
from top_photo import best_photos
from returns_10_people import return_love
from search_love import query_people


data_user = [53083705, '14.9.1965', 1, 1, 2, 54]


class Test_class(unittest.TestCase):
    """Тестирование приложения VKinder"""


    def test_main_info(self):
        """Тест функции сбора информации пользователя"""
        self.assertEqual(main('dm'), data_user)


    def test_search_love(self):
        """Тест функции возврата людей для пльзователя"""
        first_people = 22851406
        self.assertEqual(first_people,query_people(data_user)[:1][0]['id'])


    def test_top_photo(self):
        """Тест функции возврата 3 луших фото"""
        top_DM_photo = ['https://sun9-4.userapi.com/c5654/u53083705/-6/z_10fad4b3.jpg',
                        'https://sun1-83.userapi.com/c836634/v836634705/4b83/wR6HIL4mLG4.jpg',
                        'https://sun1-25.userapi.com/c626216/v626216705/2327/3SQFxgpSJ9k.jpg']
        self.assertEqual(top_DM_photo, best_photos(53083705))


    def test_returns_10_people(self):
        """Тест функции возврата сформированного результата"""
        data = [{'id': 22851406, 'first_name': 'Anny', 'last_name': 'May',
                 'track_code': '512d1481abt_V_icsNjHCsIe2RPu6Q3Q6qtZdj1hQlgttzn-HvcKwX8Hls-12cEM9tQY35iNEM_nvCt4'}]
        result = [{'favorite': 0,
                'id': 1,
                'link': 'https://vk.com/id22851406',
                'photo':
                       ['https://sun1-90.userapi.com/c637819/v637819406/3c66b/iNj0-M2Bwhw.jpg',
                        'https://sun1-26.userapi.com/c637818/v637818406/45b7e/uu7eSE827jw.jpg',
                        'https://sun1-85.userapi.com/c636718/v636718406/36f82/PK1n_xkWB3s.jpg']}]
        self.assertEqual(return_love(1, data), result)