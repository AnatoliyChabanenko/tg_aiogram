import kakieto_funk as fu
import config2
import logging
import keybord_my as kb
from google import proschet
from sqlighter import SQLighter
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from parsing_class import Nibulon

logging.basicConfig(level=logging.INFO)

# инитицеализация бота
bot = Bot(token=config2.TOKEN)
dp = Dispatcher(bot)
db = SQLighter('db.db')
nb = Nibulon()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.markup5)


@dp.message_handler(commands=['Пшениця'])
async def process_command(message: types.Message):
    await message.reply(fu.praice('Пшениця 2-го класу'), reply_markup=kb.markup5)


@dp.message_handler(commands=['Ячмень'])
async def process_command(message: types.Message):
    await message.reply(fu.praice('Ячмінь'), reply_markup=kb.markup5)


@dp.message_handler(commands=['Подсолнух'])
async def process_command(message: types.Message):
    await message.reply(fu.praice('Соняшник (закупівля здійснюється лише від товаровиробників!)'), reply_markup=kb.markup5)


@dp.message_handler(commands=['geo'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга",
                        reply_markup=kb.markup_request)


@dp.message_handler(content_types=['location'])
async def handle_loc(message):
    km = float(proschet(message.location))
    await message.reply(f'к выгрузке {km}км, перевозка транспортом обойдется {km*100}', reply_markup=kb.markup5)


@dp.callback_query_handler(lambda c: c.data == 'bot1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_kb_full)


# активация
@dp.message_handler(commands=['subscribe'])
async def subscribe(massage: types.Message):
    if not (db.subscriber_exists(massage.from_user.id)):
        db.add_subscriber(massage.from_user.id)
    else:
        db.update_subscription(massage.from_user.id, True)

        await massage.answer('отлично')


@dp.message_handler(commands=['unsubscribe'])
async def subscribe(massage: types.Message):
    if not (db.subscriber_exists(massage.from_user.id)):
        db.add_subscriber(massage.from_user.id, False)
        await massage.answer('Вы и так не пописаны.')
    else:
        db.update_subscription(massage.from_user.id, False)

        await massage.answer('Вы успешно отписались ')


async def my_parsing(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        nb.update_content()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(my_parsing(10000))
    executor.start_polling(dp, skip_updates=True)
