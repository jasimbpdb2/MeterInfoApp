[app]
# Title of your application
title = BPDB Meter Checker

# Package name (Use lowercase letters only as per Android requirements)
package.name = bpdbmeter

# Package domain
package.domain = org.bpdb

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,ttf

# Application version
version = 1.0.0

# Requirements (urllib3 is usually included with requests, no need to list separately)
requirements = python3,requests

# Android specific configurations
# (Ensure permissions don't have spaces if listed on one line, or use separate lines)
android.permissions = INTERNET, ACCESS_NETWORK_STATE 

# Target API level for Android 15
android.api = 35

# Minimum API level (23 is often a better modern minimum)
android.minapi = 23

# SDK version to use (matches target API)
android.sdk = 35

# NDK version (r25c is fine, but r26b is the latest recommended for API 34+)
android.ndk = 26b 

# Application icon
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/icon.png

# Orientation
orientation = portrait

# Fullscreen (Set to 1 if you want the app to be truly full screen)
fullscreen = 0 

# Presplash screen color
presplash.color = #FFFFFF

# Accept SSL certificates (Not recommended for production, better to use proper certs)
android.accept_ssl_cert = True

# Allow backup (generally okay)
android.allow_backup = true

# Gradle dependencies (Typically only needed if you are using specific Java libraries not handled by buildozer/python-for-android)
android.gradle_dependencies = 

# Architectures (armeabi-v7a is usually sufficient if you are just using Python and Kivy)
# arm64-v8a is the modern standard requirement for Play Store uploads
android.arch = arm64-v8a, armeabi-v7a

[buildozer]
# Log level (1 is usually enough for normal builds)
log_level = 1

# Warn if buildozer is run as root
warn_on_root = 1
