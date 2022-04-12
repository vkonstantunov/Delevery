from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_users = KeyboardButton('Пользователи')
restoran1 = KeyboardButton('Шоколадница')
restoran2 = KeyboardButton('Кофе Хауз')
restoran3 = KeyboardButton('Ваби-Саби')
replykb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(restoran1,restoran2,restoran3)
replykb1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(restoran1)






#def basket(data):
    #markup = InlineKeyboardMarkup()  # создаём клавиатуру
    #markup.row_width = 1  # кол-во кнопок в строке
    #for i in data:  # цикл для создания кнопок
        #markup.add(InlineKeyboardButton(i[1], callback_data=i[2]))
    #return markup  # возвращаем клавиатуру