from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import themes_callback
from keyboards.inline.konspekts import *

from aiogram.types import CallbackQuery

from loader import dp

@dp.callback_query_handler(themes_callback.filter(item_name = 'stepen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=stepen)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'odnochlen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=odnochlen)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'mnogochlen'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=mnogochlen)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'razloj_mnojiteli'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=razloj_mnojiteli)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'formula_umnoj'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=formula_umnoj)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'algebra_drobi'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=algebra_drobi)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'lin_uravneniya'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=lin_uravneniya)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'sistema_lin_urav'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=sistema_lin_urav)
    await call.message.delete()

@dp.callback_query_handler(themes_callback.filter(item_name = 'lin_func'))
async def buying_corse(call: CallbackQuery, callback_data: dict):
    await call.message.answer('В процессе скоро все дополним ...')
    # await call.message.answer('Выберите что вам нужно', reply_markup=lin_func)
    await call.message.delete()
