
from imports import *

#вклюаем логировния чтобы не пропустить важные сообщение
logging.basicConfig(level=logging.INFO)
#bot's object
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Записаться на прием"),
            types.KeyboardButton(text="Регистрация стоматологии")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите ваше действие"
    )
    await message.answer("Начинаем работу с ботом", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

#хэндлер на команду /test1


# Хэндлер на команду /test2






@dp.message(F.text, Command("test"))
async def any_message(message:Message):
    await message.answer(
        "Hello, <b>world</b>!",
        parse_mode=ParseMode.HTML
    )

#Отправка заранее заданного сообщения в канал keyChannel
@dp.message(Command("diceC"))
async def cmd_diceC(message: types.Message, bot: Bot):
    await bot.send_dice(keyChannel, emoji="🎲")

#Экранирование ввод, отправка сообщения, в котором текст заранее не известен

#такой же форматированный текст как и тот что рпишел
# @dp.message(F.text)
# async def echo_with_time(message: Message):
#     time_now = datetime.now().strftime('%H:%M')
#
#     added_text = html.underline(f"Создано в {time_now}")
#     await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")

if __name__ == "__main__":
    asyncio.run(main())