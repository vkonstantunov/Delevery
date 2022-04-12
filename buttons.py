from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


menu =  KeyboardButton('Меню')
help = KeyboardButton('Помощь')
basket = KeyboardButton('Корзина')
finish = KeyboardButton("Оформить заказ")
restoran1 = KeyboardButton('Ресторан1')
restoran2 = KeyboardButton('Ресторан2')
restoran3 = KeyboardButton('Ресторан3')
replykb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(menu,help,basket,finish)
replykb1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(restoran1,restoran2,restoran3)



def button(name):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(f"{name}", callback_data="call"))
    return markup


def basket(data):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    for i in data:  # цикл для создания кнопок
        markup.add(InlineKeyboardButton(i[1], callback_data=i[2]))
    return markup  # возвращаем клавиатуру