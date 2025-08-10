[app]
# Basic app info
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Target Android API 35
android.api = 35
android.minapi = 23
android.build_tools = 35.0.0
android.ndk = 27.0.12077973
android.ndk_api = 23

# Remove SDK/NDK interpolation
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/ndk/27.0.12077973

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET