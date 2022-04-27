from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_fantasy, URL_historycal, URL_horror, URL_comedy, URL_action

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Comedy", callback_data=buy_callback.new(item_name="Comedy", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Action ", callback_data="buy:Action:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Horror", callback_data="buy:Horror:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Fantasy", callback_data="buy:Fantasy:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Historical", callback_data="buy:Historical:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_comedy)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_action)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_fantasy)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_horror)
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_historycal)
    ]
])
def apples_keyboard():
    return None