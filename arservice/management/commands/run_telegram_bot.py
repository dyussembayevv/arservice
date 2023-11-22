from django.core.management import BaseCommand
import telebot
from arservice.models import University

bot = telebot.TeleBot("6921884224:AAEctz2eFB6njVBvzhU-yKPNj1v8cCIpv5c")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello World")


@bot.message_handler(commands=["universities"])
def show_uni(message):
    universities = University.objects.all()
    for university in universities:
        bot.send_message(message.chat.id, university.name)


@bot.message_handler(commands=["help"])
def show_uni(message):
    bot.send_message(message.chat.id, "/start; /universities; /help")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I don't understand. Please use the commands. To see all the commands use /help")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Started bot")
        bot.polling()
        print("Bot stopped")