import telebot 
from telebot import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnmenu = types.KeyboardButton('⚙Меню')
menu.add(btnmenu)

podmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
accaunt = types.KeyboardButton('💳Приобрести аккаунты')
nakrutka = types.KeyboardButton('🤑Приобрести гемы')
about = types.KeyboardButton('🗂О нас')
support = types.KeyboardButton('🆘Тех.поддержка')
test = types.KeyboardButton('Test')
podmenu.add(accaunt,nakrutka,about,support)

back =  types.ReplyKeyboardMarkup(resize_keyboard=True)
backbtn= types.KeyboardButton('⬅️Назад')
back.add(backbtn)



accaunts1= types.ReplyKeyboardMarkup(resize_keyboard=True)
a1 = types.KeyboardButton('Аккаунт 1')
a2 = types.KeyboardButton('Аккаунт 2')
a3 = types.KeyboardButton('Аккаунт 3')
a4 = types.KeyboardButton('Аккаунт 4')
a5 = types.KeyboardButton('Аккаунт 5')
a6 = types.KeyboardButton('Аккаунт 6')
a7 = types.KeyboardButton('Аккаунт 7')
a8 = types.KeyboardButton('Аккаунт 8')
a9 = types.KeyboardButton('Аккаунт 9')
a10 = types.KeyboardButton('Аккаунт 10')
next = types.KeyboardButton('➡️Дальше')
accaunts1.add(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,backbtn,next,)

accaunts2= types.ReplyKeyboardMarkup(resize_keyboard=True)
a11 = types.KeyboardButton('Аккаунт 11')
a12 = types.KeyboardButton('Аккаунт 12')
a13 = types.KeyboardButton('Аккаунт 13')
a14 = types.KeyboardButton('Аккаунт 14')
a15 = types.KeyboardButton('Аккаунт 15')
a16 = types.KeyboardButton('Аккаунт 16')
a17 = types.KeyboardButton('Аккаунт 17')
a18 = types.KeyboardButton('Аккаунт 18')
a19 = types.KeyboardButton('Аккаунт 19')
a20 = types.KeyboardButton('Аккаунт 20')
backinfspisok= types.KeyboardButton('⬅️Вернуться к предыдущему списку')
accaunts2.add(a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,backinfspisok)



checkback = types.ReplyKeyboardMarkup(resize_keyboard=True)
checkbtn=types.KeyboardButton('✅Проверить оплату')
backinacc = types.KeyboardButton('⬅️Вернуться к списку аккаунтов')
checkback.add(checkbtn,backinacc)

checkback2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
backinsspisok = types.KeyboardButton('⬅️Вернуться ко второму списку')
checkback2.add(checkbtn,backinsspisok)

gems = types.ReplyKeyboardMarkup(resize_keyboard=True)
g30 = types.KeyboardButton('30 Гемов')
g80 = types.KeyboardButton('80 Гемов')
g170 = types.KeyboardButton('170 Гемов')
g360 = types.KeyboardButton('360 Гемов')
g950 = types.KeyboardButton('950 Гемов')
g2000 = types.KeyboardButton('2000 Гемов')
gems.add(g30,g80,g170,g360,g950,g2000,backbtn)

checkback3= types.ReplyKeyboardMarkup(resize_keyboard=True)
backingems = types.KeyboardButton('⬅️Вернуться к гемам')
checkback3.add(checkbtn,backingems)