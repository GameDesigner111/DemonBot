from dotenv import load_dotenv
import telebot
import os
import schedule
import time


def main():
    load_dotenv()
    tgkey = os.getenv("TG_TOKEN")
    chadid = os.getenv("USER_ID") 

    bot = telebot.TeleBot(tgkey)
    bot.send_message(chadid, text="good morning")


if __name__ == '__main__':
    timemsg = os.getenv("MSG_TIME") 

    schedule.every().day.at("19:25", "Europe/Moscow").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
