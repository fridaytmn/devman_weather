# devman_weather

## Description
devman_weather is a small script that outputs weather in three default locations: London, UK, Sheremetievo Moscow Airport (code SVO) and Cherepovets, Russia.
The script uses the API of the wttr.in Web service. The locations are easily editable in the main.py file.

## How to install
You need Python 3 to execute this script. If Python 3 is not yet installed then download it from http://www.python.org for your operating system and install.

After install Python 3 need use this command

For Windows:
```sh
py -m pip install -r requirements.txt
```
For Unix/MacOS
```sh
python -m pip install -r requirements.txt
```

## How to launch

```sh
python3 main.py
```

If you use a *nix-based operating system, you can do the following in your terminal:

```sh
chmox +x main.py
```

After this you will be able to execute the script by typing ./main.py in your terminal (as long as you are in the script's directory).
