import logging

from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback

from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard

from loader import dp, bot

@dp.message_handler(Command("start"))

async def show_items(message: Message):

    await message.answer(text="Choose one of dorama genres:",

                         reply_markup=choice)

@dp.callback_query_handler(text_contains="Comedy")

async def buying_pear(call: CallbackQuery):

    await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.answer("you chose Comedy doramas. Good_luck.",

                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="Action"))

async def buying_apples(call: CallbackQuery, callback_data: dict):

    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")

    quantity = callback_data.get("quantity")

    await call.message.answer(f"You chose action doramas. Good luck.",

                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="horror"))

async def buying_apples(call: CallbackQuery, callback_data: dict):

    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")

    await call.message.answer(f"You chose horror doramas. Good luck.",

                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="Fantasy"))

async def buying_apples(call: CallbackQuery, callback_data: dict):

    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")

    await call.message.answer(f"You chose Fantasy. Good luck.",

                              reply_markup=apples_keyboard)

    @dp.callback_query_handler(buy_callback.filter(item_name="Historical"))
    async def buying_apples(call: CallbackQuery, callback_data: dict):
        await call.answer(cache_time=60)

        logging.info(f"{callback_data=}")

        await call.message.answer(f"You chose historical doramas. Good luck.",

                                  reply_markup=apples_keyboard)

@dp.callback_query_handler(text="cancel")

async def cancel_buying(call: CallbackQuery):

    await call.answer("You've Canceled!",

                      show_alert=True)

    await  call.message.edit_reply_markup(reply_markup=None)