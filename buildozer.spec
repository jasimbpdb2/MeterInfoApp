[app]
title = MyApp
package.name = myapp
package.domain = org.example
version = 1.0.0

# API & Build Tools
android.api = 35
android.minapi = 23
android.build_tools = 35.0.0
android.ndk = 27.0.12077973
android.ndk_api = 23

# Remove ROOT substitutions — we'll set these in GitHub Actions env
# android.sdk_path = %(ANDROID_SDK_ROOT)s   <-- REMOVE
# android.ndk_path = %(ANDROID_NDK_ROOT)s   <-- REMOVE

orientation = portrait
android.permissions = INTERNET