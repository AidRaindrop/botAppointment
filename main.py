
from imports import *

#вклюаем логировния чтобы не пропустить важные сообщение
logging.basicConfig(level=logging.INFO)
#bot's object
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

async def main():
    await dp.start_polling(bot)

#хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

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
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, {html.bold(html.quote(message.from_user.full_name))}",
    )

@dp.message(F.text)
async def echo_with_time(message: Message):

if __name__ == "__main__":
    asyncio.run(main())