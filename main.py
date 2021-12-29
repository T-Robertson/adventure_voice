import os
import time
import random
import playsound
import speech_recognition as sr
import pyttsx3

### This voice input system is from TechwithTim
class voice_input_output:
    def speak(self,text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print('Player said: '+ said)
            except Exception as e:
                print("Exception: " + str(e))
        return said.lower()

class main_game:
    def __init__(self):
        #Player's Stats
        self.player_health = 100
        self.player_stamina = 100
        
        #Storyline
        self.storyline_parts = []
        self.parts_reader()
    
    #Reads txt file for output lines 
    def parts_reader(self):
        x = 0
        with open('parts_lines.txt', 'r') as file:
            for lines in file:
                parts = lines.rstrip()
                self.storyline_parts.insert(x,parts)
                x +=1
        file.close()            
    
    #Main, handles the game
    def main(self):
        self.storyline()
        
    #Player input commands, outputs are def before if statements
    def player_commands(self, command):
        player_stats = f'Players health is {self.player_health} and players stamina is {self.player_stamina}'
        
        if "stats" in command:
            voice_input_output().speak(player_stats)
            print(player_stats)
    
    #Main storyline, reads outputs to the player and looks for inputs 
    def storyline(self):
        x = 0 
        for parts in self.storyline_parts:
            voice_input_output().speak(self.storyline_parts[x])
            x += 1
            player_input = voice_input_output().get_audio()
            self.player_commands(player_input)
            


def main():
    game = main_game()
    game.__init__()
    game.main()

if __name__ == '__main__':
    main()