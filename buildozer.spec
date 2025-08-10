[app]
title = MeterInfo
package.name = meterinfo
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,urllib3
orientation = portrait

# Target Android 15 (API 35)
android.api = 35
android.build_tools = 35.0.0
android.ndk = 26.1.10909125

# Correct NDK & SDK path usage
android.sdk_path = %(ANDROID_SDK_ROOT)s
android.ndk_path = %(ANDROID_NDK_ROOT)s

# Optional permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0