import psycopg2 as pg
from data_base_VKinder.db_connect import database_con as login


with pg.connect(database=login['database'], user=login['user'],
                password=login['password'], host=login['host'], port=login['port']) as conn:
    cur = conn.cursor()


def create_user():
    """Cоздание профиля"""
    cur.execute('''
        create table if not exists User_vkinder(us_id serial primary key,
        name_id integer not null,
        birth timestamp with time zone null,
        city integer not null,
        country integer not null,
        gender integer not null);''')
    conn.commit()


def add_user(data):
    """Добавляет профиль"""
    try:
        #если профиль уже создан, не создавать новый с новым primary key
        cur.execute('select * from User_vkinder where name_id=(%s);', (data[0],))
        pr_key = cur.fetchall()[0][0]
    except:

        cur.execute('''
                    insert into User_vkinder(name_id, birth, city, country, gender) values(%s, %s, %s, %s, %s);''',
                    (int(data[0]), data[1], int(data[2]), int(data[3]), int(data[4])))
        conn.commit()
        cur.execute('select * from User_vkinder where name_id=(%s);', (data[0],))
        pr_key = cur.fetchall()[0][0]
    return pr_key


def create_people_table():
    """Cоздание таблицы людей, просмотренных пользователем"""

    cur.execute('''
    create table if not exists People_vkinder(
    sid integer references User_vkinder(us_id),
    id_vk varchar(35) not null,
    photo text not null,
    favorite integer not null); ''')
    conn.commit()


def add_people(data_people):
    """Добавление людей, просмотренных пользователем"""

    for people in data_people:
        cur.execute('''
                    insert into People_vkinder(sid, id_vk, photo, favorite) values(%s, %s, %s, %s);''',
                    (people['id'], people['link'], people['photo'], int(people['favorite'])))
    conn.commit()
