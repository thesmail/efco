# -*- coding: utf-8 -*-

from enum import Enum
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


TOKEN = '983071785:AAE-4gKtJpp7PA1wLtcXUtdvUz9duTP1BnA'
db_file = "config/database.vdb"

data = {'xLogin': 'evgen28rus@mail.ru', 'xPassword': 'had2911'}

rel_path = "bet_num.txt"
abs = os.path.join(script_dir, rel_path)

f = open(os.path.join(script_dir, 'bet_num.txt'), 'r')
sumBet = int(f.read())
f.close()#кол-во необходимых заявок

price = '10'

class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_CITY = "1"
