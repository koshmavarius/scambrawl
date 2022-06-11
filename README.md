# scambrawl

Установка:

apt update

apt upgrade

git clone https://github.com/koshmavarius/scambrawl

cd scambrawl

pip install -r requirements.txt

python scambrawl.py


Как исправить ошибку Telebot object has no attribute
message_handler:

pip3 uninstall telebot
pip3 uninstall PyTelegramBotAPI
pip3 install pyTelegramBotAPI
pip3 install --upgrade pyTelegramBotAPI


