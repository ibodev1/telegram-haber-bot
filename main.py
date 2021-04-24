import constants as keys
import responses as R
from telegram.ext import *
import requests
from bs4 import BeautifulSoup

print("Bot çalışıyor...")


def start_command(update, context):
    update.message.reply_text('Merhaba Hoşgeldin. \n/sonhaber \n/tumu')

def son_haber(update, context):
    r = requests.get("https://www.cumhuriyet.com.tr/gundem")
    s = BeautifulSoup(r.content,"lxml")
    haber = s.find("div",attrs={"class":"haber"})
    haber_foto = haber.find("div",attrs={"class":"haber-foto"}).find("img")
    haber_baslik = haber.find("div",attrs={"class":"haber-baslik"}).find("a")
    update.message.reply_text(haber_baslik.get("title") + "\n \n Haber Link : " + "https://www.cumhuriyet.com.tr"+ str(haber_baslik.get("href")) + "\n \n Resim Link : " + "https://www.cumhuriyet.com.tr"+ str(haber_foto.get("src")))
    pass

def tumu(update, context):
    r = requests.get("https://www.cumhuriyet.com.tr/gundem")
    s = BeautifulSoup(r.content,"lxml")
    haber = s.find_all("div",attrs={"class":"haber"})
    for news in haber:
        news_image = news.find("div",attrs={"class":"haber-foto"}).find("img")
        news_title = news.find("div",attrs={"class":"haber-baslik"}).find("a")
        update.message.reply_text(news_title.get("title") + "\n \n Haber Link : " + "https://www.cumhuriyet.com.tr"+ str(news_title.get("href")) + "\n \n Resim Link : " + "https://www.cumhuriyet.com.tr"+ str(news_image.get("src")))
    update.message.reply_text("Haber Sayısı : " + str(len(haber)))
    pass

def help_command(update, context):
    update.message.reply_text('/sonhaber : Son Haberi Çeker \n/tumu : Tüm Haberleri Çeker')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update : {update} Error : {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("basla", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("yardim", help_command))
    dp.add_handler(CommandHandler("sonhaber", son_haber))
    dp.add_handler(CommandHandler("tumu", tumu))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

