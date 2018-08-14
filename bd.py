import sqlite3

'''Создание базы данных'''
conn = sqlite3.connect('ourdatabase.db', check_same_thread=False)
cursor = conn.cursor()
'''Создание таблицы users'''
cursor.execute("""CREATE TABLE IF NOT EXISTS CUSTOMER
(id integer, username text, first_name text, last_name text, telephone_num text,
 request integer, status integer, points integer)
 """)
#cursor.execute("""DROP TABLE users""")
'''Таблица квестов'''
cursor.execute("""CREATE TABLE IF NOT EXISTS QUESTS
(id integer, stage integer, quest_num integer)""")
'''Таблица обратной связи'''
cursor.execute("""CREATE TABLE IF NOT EXISTS FEEDBACK
(id integer, mark integer, comment text)""")
'''Таблица ответов'''
cursor.execute("""CREATE TABLE IF NOT EXISTS ANSWERS
(quest_num integer, stage integer, answer text)""")
'''Вставка пользователя'''


def insert_user(id):
    q = 'SELECT EXISTS (SELECT * FROM CUSTOMER WHERE id={})'.format(id)
    cursor.execute(q)
    info = cursor.fetchall()
    if info[0][0] == 0:
        new_user = (id, '', '', '', '', 0, 0, 0)
        comand = 'INSERT INTO CUSTOMER VALUES {}'.format(new_user)
        cursor.execute(comand)
    else:
        pass
    conn.commit()
    cursor.execute('SELECT request FROM CUSTOMER WHERE id={}'.format(id))
    info_request = cursor.fetchall()
    return (info[0][0], info_request[0][0])


#print(insert_user(1))
'''2)Заполнение основной инфы'''


def insert_info(id, username, first_name, last_name):
    if username is None:
        username = ''
    if first_name is None:
        first_name = ''
    if last_name is None:
        last_name = ''
    q = '''UPDATE CUSTOMER SET username = '{}', 
    first_name = '{}', last_name = '{}' 
    WHERE id={}'''.format(username, first_name, last_name, id)
    cursor.execute(q)
    conn.commit()


insert_info(1, "MAK", 'Anton', None)
'''Запонение номера телефона'''


def insert_phone(id, phone_num):
    q = '''UPDATE CUSTOMER SET telephone_num = '{}'
    WHERE id={}'''.format(phone_num, id)
    cursor.execute(q)
    conn.commit()


insert_phone(1, '89091687375')
'''Изменение очков'''


def change_points(id, count):
    q = 'SELECT points FROM CUSTOMER WHERE id={}'.format(id)
    cursor.execute(q)
    old_points = cursor.fetchall()[0][0]
    new_points = old_points + count
    comand = 'UPDATE CUSTOMER SET points={} where id={}'.format(new_points, id)
    cursor.execute(comand)
    conn.commit()


'''Возврат очков'''


def come_back_points(id):
    q = 'SELECT points FROM CUSTOMER WHERE id={}'.format(id)
    cursor.execute(q)
    return cursor.fetchall()[0][0]


'''Список лидеров, возвращает список кортежей из 3-х элементов'''


def list_of_leaders(count):
    cursor.execute('SELECT first_name, last_name, points '
                   'FROM CUSTOMER '
                   'ORDER BY points DESC LIMIT {}'.format(count))
    return (cursor.fetchall())


'''Список лидеров по username'''


def list_of_usernames(count):
    cursor.execute('SELECT username, points '
                   'FROM CUSTOMER '
                   'ORDER BY points DESC LIMIT {}'.format(count))
    return (cursor.fetchall())


def back_quest(id):
    cursor.execute('SELECT request, quest_num, stage '
                   'FROM CUSTOMER INNER JOIN QUESTS '
                   'ON CUSTOMER.id=QUESTS.id '
                   'WHERE CUSTOMER.id={}'.format(id))
    return cursor.fetchall()


print(back_quest(1))
'''Возвращает этап квеста, на котором находится игрок'''


def back_of_stage(id, number_of_quest):
    cursor.execute('SELECT stage from QUESTS where id={} and quest_num={}'.format(id, number_of_quest))
    return cursor.fetchall()

