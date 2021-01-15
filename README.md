# Mock GUI for a pressure adsorption oxygen generator in PyQT5(Python3)

## Contains

- PyQT5 UI files
- Pyuic5 generated skeleton files
- Controller app for calling skeletons

## Demonstrates

- login using SHA256 passwords(Python Passlib)
- Python stdiomask to mask passwords on commandline(app.py)
- PyQT5 windows, message boxes, dialogs and signals
- Python threads(todo)

## How to use

- app.py is a simple app to update the password. Username is user and default password is 1234. Password hash file will be created on first call to login API.
- app_ui.py calls the PyQT5 GUI. Call app.py to update to numeric password if changed, since keypad only supports numeric passwords.

## Generating a py file from QT ui file

Run the following command(Make sure PyQT5 is installed):

```bash
pyuic5 .\keypadlock.ui -o keypad.py -x
```

## Pip Requirements

- PyQT5
- stdiomask
- Passlib
