[app]
# (str) Title of your application
title = MeterInfoApp
source.dir = .
version = 0.1

# (str) Package name
package.name = meterinfoapp

# (str) Package domain (unique, change to your own domain if desired)
package.domain = org.example

# (str) Source files to include in your package
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add all pure-python and kivy dependencies _comma-separated_!
requirements = python3,kivy,requests,urllib3

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported Android SDK version
android.api = 35

# (str) Android NDK version to use
android.ndk = 25b

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android entry point
entrypoint = main.py
