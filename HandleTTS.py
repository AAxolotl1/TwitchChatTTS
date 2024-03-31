#Skeleton of the file created by DougDoug and later updated by AAxolotl1 to turn messages into audio.
import configparser
import Twitch_Connection
import random
import keyboard
from gtts import gTTS
from io import BytesIO
from pygame import mixer

class TTS:
    def __init__(self):
        #Setup ConfigParser to read in data from Settings.ini
        self.settingsFile = 'Settings.ini'
        self.settings = configparser.ConfigParser()
        self.settings.read(self.settingsFile)

        #Read in settings using the ConfigParser
        self.twitchName = self.setTwitchName(self.settings.get('Settings', 'Channel_Name'))

        try:
            self.ttsChance = float(self.settings.get('Settings', 'TTS_Chance'))
        except:
            self.ttsChance = self.setTTSChance(input("TTS Chance is not a vaild number. Please input a value between 0 & 1: "))
        
        try:
            self.volume = int(self.settings.get('Settings', 'Volume'))
        except:
            self.volume = self.setVolume(input('Volume was not set at a valid number. Please choose a number between 0 and 100'))

        #Connect to your twitch channel
        self.t = Twitch_Connection.Twitch()
        self.t.twitch_connect(self.twitchName)
        mixer.init()

    #Setters for class variables
    def setTwitchName(self, capture):
        self.settings.set('Settings', 'Channel_Name', capture)
        with open(self.settingsFile, 'w') as configfile:
            self.settings.write(configfile)
        return capture
        
    def setTTSChance(self, capture):
        while True:
            try:
                while True:
                        capture = float(capture)
                        if capture > 0 and capture <= 1:
                            self.settings.set('Settings', 'TTS_Chance', str(capture))
                            with open(self.settingsFile, 'w') as configfile:
                                self.settings.write(configfile)
                            return capture
                        else:
                            capture = input("Please Input a value between 0 & 1: ")
            except:
                capture = input("Please input a value between 0 & 1: ")
    
    def setVolume(self, capture):
        while True:
            try:
                while True:
                    capture = int(capture)/100
                    if capture >= 0 and capture <= 1:
                        self.settings.set('Settings', 'Volume', str(capture * 100))
                        with open(self.settingsFile, 'w') as configfile:
                            self.settings.write(configfile)
                        return capture
                    else: capture = input("Please input a value between 0 & 100: ")
            except:
                capture = input("Please choose a number between 0 & 100: ")
    
    #Read in messages and convert them into audio
    def RunTTS(self):
        while True:
            messages = self.t.twitch_receive_messages()

            if not messages:
                if keyboard.is_pressed('shift+backspace'):
                    break
                else:
                    continue
            else:
                try:
                    for message in messages:
                        if keyboard.is_pressed('shift+backspace'):
                            break

                        if random.random() < self.ttsChance:
                            
                            msg = message['message'].lower()
                            username = message['username'].lower()

                            print("Recieved message from " + username + ": " + msg)

                            tts = gTTS(text=msg, lang='en')
                            mp3 = BytesIO()
                            tts.write_to_fp(mp3)
                            mp3.seek(0)

                            sound = mixer.Sound(mp3)
                            sound.set_volume(self.volume)
                            sound.play()
                            mp3.close()
                except Exception as e:
                    print("Encountered an error: " + str(e))

#Class for ConfigureTTS.py                    
class TTSConfigure(TTS):
    def __init__(self):
        self.settingsFile = 'Settings.ini'
        self.settings = configparser.ConfigParser()
        self.settings.read(self.settingsFile)

        self.twitchName = self.setTwitchName(input("Please input your twitch username (or twitch channel you want to connect Text-to-Speech to): "))
        self.ttsChance = self.setTTSChance(input("Please choose a number between 0 to 1 to set as your Text-to-Speech chance: "))
        self.volume = self.setVolume(input("Please choose a number between 0 & 100: "))

        self.t = Twitch_Connection.Twitch()
        self.t.twitch_connect(self.twitchName)
        mixer.init()

