[app]
title = MyApp
package.name = myapp
package.domain = org.example
version = 1.0.0
source.dir = .

# API & Build Tools
android.api = 36
android.minapi = 23
#android.build_tools = 35.0.0-rc2
#android.ndk=26.1.10909125
android.ndk_api = 25b
android.sdk = 34

# Remove ROOT substitutions — we'll set these in GitHub Actions env
# android.sdk_path = %(ANDROID_SDK_ROOT)s   <-- REMOVE
# android.ndk_path = %(ANDROID_NDK_ROOT)s   <-- REMOVE

orientation = portrait
android.permissions = INTERNET