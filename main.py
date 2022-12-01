from db import cursor, conn
from telebot import types

def create_table_user():
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        prohe_number VARCHAR(255) NOT NULL,
        frist_name VARCHAR,
        last_name VARCHAR,
        chat_id INT);"""
    
    cursor.execute(query = query)
    conn.commit()
    print('create table user success!')
    
def insert_user(
                phone_number: str,
                first_name: str,
                last_name: str,
                chat_id: int):
    query = f"""
    INSERT INTO users (
        prohe_number, frist_name, last_name, chat_id
    )VALUES (
        '{phone_number}', '{first_name}', '{last_name}', {chat_id}
        );"""
    cursor.execute(query=query)
    conn.commit()
    print('insert user success!')
    
def is_user_exist(chat_id: int) -> bool:
    query = f"""
    SELECT *
    FROM users
    WHERE chat_id = {chat_id};"""
    cursor.execute(query=query)
    response = cursor.fetchone()
    if response is not None:
        return True
    return False

def create_inline_markup(row_width: int, **kwargs):
    markup = types.InlineKeyboardMarkup(row_width=row_width)
    items = []
    for key, value in kwargs.items():
        item = types.InlineKeyboardButton(value, callback_data=key)
        items.append(item)
    markup.add(*items)
    return markup
