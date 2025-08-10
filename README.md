# Meter Info App (Kivy, Android APK)

A simple Kivy Android app to check meter information via BPDB prepaid API.

## Features
- Enter meter number and view info
- Tap table cells to select/unselect
- View last 3 recharges

## Requirements
- Python 3
- Kivy, Buildozer (for APK build)

## How to Build APK

1. Clone and enter project directory:
    ```sh
    git clone https://github.com/YourUsername/MeterInfoApp.git
    cd MeterInfoApp
    ```
2. Install Buildozer & dependencies (on Ubuntu/WSL):
    ```sh
    sudo apt update
    sudo apt install python3-pip openjdk-17-jdk
    pip3 install kivy buildozer
    ```
3. Edit `buildozer.spec` (update requirements, icons, etc.)
4. Build the APK:
    ```sh
    buildozer -v android debug
    ```
5. APK will be in the `bin/` folder!

## Notes

- Linux (or WSL) required for building
- For help, refer to [Kivy packaging Android](https://kivy.org/doc/stable/guide/packaging-android.html)

## License

MIT
