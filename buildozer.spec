[app]
title = Calculator
package.name = calculator
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt
version = 0.1.0
orientation = portrait
fullscreen = 0
log_level = 2
requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
android.ndk_api = 21
android.archs = armeabi-v7a, arm64-v8a
android.permissions =
android.accept_sdk_license = True
