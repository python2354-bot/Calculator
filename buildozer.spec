[app]
title = CalcApp
package.name = calcapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,atlas,txt,md
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
log_level = 2
android.api = 34
android.minapi = 24
# Use build-tools 30.0.3 because it's well-tested with p4a
android.build_tools_version = 30.0.3
android.accept_sdk_license = True
android.enable_androidx = True
# Build only for 64-bit ARM to speed up CI
arch = arm64-v8a

# (Optional) Icon - place icon.png in the project root and uncomment
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 0