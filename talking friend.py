# FRIEND APP

import speech_recognition as sr
import pyttsx3 
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener =sr.Recognizer()

speaker =pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
                       #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate


def speak(text):
    speaker.say('yes Boss,', text)
    speaker.runAndWait()

def speak_ex(text):
   speaker.say(text)
   speaker.runAndWait()



va_name = 'jarvis'

speak_ex('i am your'+va_name+',Tell me boss.')

def take_command():
   command=''

   try:
      with sr.Microphone() as source:
        print('listen..')
        voice=listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if va_name in command:
            command=command.replace(va_name+' ','')
            #print(command)
            #speak(command)
   except:
      print('check your microphone') 
   return command
 #function call

while True:  #while until tell
    user_command=take_command()
    if 'close' in user_command:
       print('See you bye bye boss')
       speak('See you bye bye boss')
       break
    elif 'time' in user_command:
       cur_time = dt.datetime.now().strftime("%I:%M %p")
       print(cur_time)
       speak(cur_time)
    elif 'play' in user_command:
       user_command= user_command.replace('play','')
       print('playing' +user_command)
       speak('playing' +user_command+',enjoy boss.') 
       pk.playonyt(user_command)
       break 

    elif 'search for' in user_command or 'google' in user_command:
       user_command=user_command.replace('search for','')
       user_command=user_command.replace('google','')           
       speak('searching for'+user_command)
       pk.search(user_command)

    elif 'who is ' in user_command:
       user_command = user_command.replace('who is','')   
       info = wiki.summary(user_command,2)
       print(info)
       speak(info)

    elif 'who are you' in user_command:
       speak_ex( 'i am your'+va_name+',Tell me boss.')
   
    else:
       speak_ex('please say it again')   
        


