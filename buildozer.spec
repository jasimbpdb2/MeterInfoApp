[app]
# Title of your application
title = BPDB Meter Checker

# Package name
package.name = bpdbmeter

# Package domain (needed for android)
package.domain = org.bpdb

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,ttf

# Application version
version = 1.0.0

# Requirements
requirements = python3,requests,urllib3

# Android specific configurations
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 35
android.minapi = 21
android.sdk = 35
android.ndk = 25c

# Application icon
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/icon.png

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Presplash screen color
presplash.color = #FFFFFF

# Accept SSL certificates (needed for your API calls)
android.accept_ssl_cert = True

# Allow backup
android.allow_backup = true

# Gradle dependencies
android.gradle_dependencies = com.android.volley:volley:1.2.1

# Architectures
android.arch = arm64-v8a, armeabi-v7a

[buildozer]
# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Warn if buildozer is run as root
warn_on_root = 1
