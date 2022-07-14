import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
from save import BotDB


#   TOKEN   #
bot = Bot(token="5385406422:AAGnCUR7gRZ8xTZgr8rdRY4NIXbktJORlNg")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


#   CONNECT  SQL   #

BotDB = BotDB('./DB/db.db')



base = sqlite3.connect('./DB/db.db')
cur = base.cursor()

'''
conn = sqlite3.connect('../RandomBot-1/DB/db.db', check_same_thread=False)
cursor = conn.cursor()

def db_tab_val(user_id: int, user_name: str, user_surname: str, username: str, us_starting:str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username, us_starting) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, us_starting))
    conn.commit()
def upd_tab_val(user_id, us_starting):
    cursor.execute("UPDATE `test` SET `us_starting` = ? WHERE `user_id` = ?", (us_starting, user_id(user_id)))
    return conn.commit()
'''



#      VARIABLE      #

count_vol = 0

a = 0


class Wait(StatesGroup):
    count_vol = State()



#      MESSAGE      #
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Добавить бота в группу", url="http://t.me/djdbddjdiekemehzoakwbot?startgroup=Lichka")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)


    await message.answer("Привет! Здесь ты можешь узнать сколько у тебя хромосом"
                         "\nОт -5, до +10 за одну команду"
                         "\nПо команде /check", reply_markup=keyboard)
    
    '''
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_tab_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    '''
@dp.message_handler(commands="check")
async def volume(message: types.Message):
    
    count_vol = 0
        
    rand = int(random.randint(-5, 10))
        
    su = rand + a + int(count_vol)  
    count_vol = int(su)
    user_id = message.from_user.id

    sel = cur.execute('SELECT count_vol = ? FROM users WHERE user_id = ?', (user_id, count_vol,))
    #def add_user(self, user_id):
        #self.cursor.execute('INSERT INTO users (user_id, count) VALUES (?, ?)', (count_vol, user_id))
        #return self.conn.commit()

    if(not BotDB.user_exists(message.from_user.id)):
        
        count_vol = 0
        
        rand = int(random.randint(-5, 10))
        
        su = rand + a + int(count_vol)  
        count_vol = int(su)
        BotDB.add_user(message.from_user.id, count_vol)

        await message.reply(f"11.{message.from_user.first_name}, твоё количство хромосом уменьшилось, их количество равно " + str(count_vol) + ' шт')
        await Wait.count_vol.set()
        
        
    if(BotDB.vol_exists(message.from_user.id)):
        
        user_id = message.from_user.id

        sel = cur.execute('SELECT count_vol FROM users WHERE user_id', (user_id, count_vol,))
        print(sel)
        count_vol = el
        
        for el in sel:
            el = int(el)
            
        rand = int(random.randint(-5, 10))
        
        su = rand + a + int(count_vol)  
        count_vol = int(su)
        BotDB.upd_vol(message.from_user.id, count_vol)
        
        await message.reply(f"22. {message.from_user.first_name}, твоё количство хромосом уменьшилось, их количество равно " + str(count_vol) + ' шт')
        await Wait.count_vol.set()
        
        
    else:
        user_id = message.from_user.id

        sel = cur.execute('SELECT count_vol FROM users WHERE user_id = ?', (user_id,))
        
        
       
        
        lol = sum(sel)
        
            
        rand = int(random.randint(-5, 10))
        count_vol = lol
        su = rand + a + int(count_vol)  
        count_vol = int(su)
        BotDB.upd_vol(message.from_user.id, count_vol)
        
        await message.reply(f"22. {message.from_user.first_name}, твоё количство хромосом уменьшилось, их количество равно " + str(count_vol) + ' шт')
        await Wait.count_vol.set()
        
        
    '''
    us_id = message.from_user.id
    count_vol = str(su)
    usvol = count_vol
    upd_tab_val(user_id=us_id, us_starting=usvol)
    '''


    
    
#      MESSAGE  FOR  DIRECT      #
'''
@dp.message_handlers(text=["start sonya"])
async def friend(message: types.Message):
    await message.reply("Привет, Соня! Ты пришла сюда из лички Ильи!) Это я знаю \nТы можешь нажать на старт ещё раз, но уже будет другое уведомление \nНажми на /check")
'''


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)