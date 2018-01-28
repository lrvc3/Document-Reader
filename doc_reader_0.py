## Document Reader 
import pyttsx3

engine = pyttsx3.init()
##
##engine.setProperty('rate',120)  #120 words per minute
##engine.setProperty('volume',0.9) 

with open("readfile.txt") as file:
    for line in file:
        engine.say(line)
        engine.runAndWait()
 
        
