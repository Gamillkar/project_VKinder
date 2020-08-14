from main_user_info import main_user_info
from search_love import query_people
from returns_10_people import return_love
from data_base_VKinder import db


class User():
    """Создание пользователя. Добавление в BD людей"""


    def __init__(self, id, year_from=None, year_to=None):
        self.id = id
        self.year_from = year_from
        self.year_to = year_to


    def main_block(self):
        """Основной блок. Взаимодействие c модулями"""
        #получение данных пользователя
        main_user = main_user_info(self.id)
        #создание профиля в BD
        db.create_user()
        pr_key = db.add_user(main_user)
        db.create_people_table()
        #получение данных 1000 человек
        people = query_people(main_user, self.year_from, self.year_to)
        #получение фото и ссылок на профиль. Сохранение в DB и JSON
        return_love(pr_key, people)


if __name__ == "__main__":
    #пользователь может самостоятельно указать диапазон возраста

    DM = User('dm', 23, 44)
    DM.main_block()




