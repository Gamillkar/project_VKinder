from main_user_info import main_user_info
from search_love import query_people




def main_block(id, year_from=None, year_to=None):

    main_user = main_user_info(id)
    query_people(main_user, year_from, year_to)



if __name__ == "__main__":
    #пользователь может самостоятельно указать диапазон возраста
    main_block('51960836', 26, 26)





