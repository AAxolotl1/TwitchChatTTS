# TwitchChatTTS
These are four python files and an INI file that handles Twitch Chat messages and converts them into Speech using Google's Text to Speech.

To run the code you will need to install Python 3.9.  
Additionally, you will need to install the following python modules using Pip:  
python -m pip install keyboard  
python -m pip install gtts  
python -m pip install pygame   

Running ConfigureTTS.py will ask for inputs to change the settings in the Settings.ini file before running the text to speech program.

Running TTS.py will automatically read in Settings.ini and run the text to speech program


This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated. I later took the Twitch portiion of the connection file and made a file that converts the data grabbed from the connection file, and converts it into Speech Audio. 
