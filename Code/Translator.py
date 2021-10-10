# Importing necessary modules required
import speech_recognition as spr
from translate import *
from gtts import gTTS
import os

# Creating a recognizer instance
recog = spr.Recognizer()

# Creating a microphone instance
mic = spr.Microphone()

# Using the mic instance created as a source to capture audio
with mic as source:
    print("Say Hello to initiate the conversation !")
    print("..........We are trying to detect your voice..........")
    
    # Eliminating echoes/gaps/disturbances in the audio being captured
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)
    
    # Converting audio recorded into lower case text
    Text = recog.recognize_sphinx(audio).lower()
    
    # Looking for prompt
    if 'hello' in Text:
        
        # Language code to be translated to - can be changed to translate to different languages
        to_lang = 'hi'
        
        # Creating a translator instance
        translator = Translator(to_lang)

        print("\nWe found you !!!!\n")

        print("Start speaking, we are translating as you speak !!")
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        lines = recog.recognize_sphinx(audio)
        
        print("Here's what we heard :", lines)
        
        # Translating input to selected output language
        translated_lines = translator.translate(lines)
        text = translated_lines
        print("\nThe translated audio should be playing in a few seconds !!")
        
        # Creating a text-to-speech instance
        speak = gTTS(text=text, lang=to_lang, slow=False)
        
        # Saving the output file onto the local computer
        speak.save("output_voice.mp3")
        
        # Playing the saved output (translated) audio file
        os.system("start output_voice.mp3 tempo")
