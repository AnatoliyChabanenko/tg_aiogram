from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton





button_hi = KeyboardButton('Привет! 👋')
button_1 =KeyboardButton('Узнать цены')
button_2 =KeyboardButton('Розщитать доставку',request_location=True)
button_3 =KeyboardButton('Связаться с вами ', request_contact=True)


button10 = KeyboardButton('/Пшениця')
button11 = KeyboardButton('/Ячмень')
button12 = KeyboardButton('/Подсолнух')

markup5 = ReplyKeyboardMarkup().row(
    button10, button11, button12
)

button6 = KeyboardButton('/geo')
markup5.insert(button6)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('пощитать доставку ', request_location=True)
)


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))

