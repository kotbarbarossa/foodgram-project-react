import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from random import randrange

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def wake_up(update, context):
    """Отправка сообщения при подключении бота."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    username = update.message.chat.username
    try:
        context.bot.send_message(
            chat_id=chat.id,
            text=f'Демон продуктовый помошник активирован >:-Е! '
            f'{name}.{username} теперь ты подписан '
            f'на демонические покупки игредиентов!'
        )
    except Exception as error:
        AssertionError(f'{error} Ошибка отправки ответа в телеграм')


def say_no(update, context):
    """Отправка рандомного ответа в чат."""
    chat = update.effective_chat
    random_answer = randrange(6)
    answers = {
        '0': 'Не прерывай чтение заклинания!',
        '1': 'Всё так же ни чего нового...',
        '2': 'Запомни: терпение и дисциплина',
        '3': 'Я знал что ты это спросишь',
        '4': 'Мы тут не для этого собрались',
        '5': 'Чем больше вопросов тем меньше ответов',
    }
    text = answers[str(random_answer)]
    try:
        context.bot.send_message(
            chat_id=chat.id,
            text=text
        )
    except Exception as error:
        raise AssertionError(f'{error} Ошибка отправки ответа в телеграм')


def send_message(message):
    """Отправка сообщения в чат."""
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as error:
        raise AssertionError(f'{error} Ошибка отправки в телеграм')


def main():
    """Основная логика работы бота."""
    UPADTER = Updater(token=TELEGRAM_TOKEN)
    UPADTER.dispatcher.add_handler(CommandHandler('start', wake_up))
    UPADTER.dispatcher.add_handler(MessageHandler(Filters.text, say_no))
    UPADTER.start_polling()
