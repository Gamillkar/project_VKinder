from main_user_info import main_user_info
from search_love import query_people
from returns_10_people import return_love




def main_block(id, year_from=None, year_to=None):
    #получение данных пользователя
    main_user = main_user_info(id)
    #получение данных 1000 человек
    people = query_people(main_user, year_from, year_to)
    #получение фото и ссылок на профиль
    return_love(people)




if __name__ == "__main__":
    #пользователь может самостоятельно указать диапазон возраста
    main_block('gamillkar', 23, 35)





