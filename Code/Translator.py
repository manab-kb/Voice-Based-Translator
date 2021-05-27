# Importing necessary modules required
import speech_recognition as spr
from translate import *
from gtts import gTTS
import os

recog = spr.Recognizer()

mic = spr.Microphone()

with mic as source:
    print("Say Hello to initiate the conversation !")
    print("..........We are trying to detect your voice..........")
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)
    Text = recog.recognize_sphinx(audio).lower()

    if 'hello' in Text:

        to_lang = 'hi'
        translator = Translator(to_lang)

        print("\nWe found you !!!!\n")

        print("Start speaking, we are translating as you speak !!")
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        lines = recog.recognize_sphinx(audio)

        print("Here's what we heard :", lines)
        translated_lines = translator.translate(lines)
        text = translated_lines
        print("\nThe translated audio should be playing in a few seconds !!")

        speak = gTTS(text=text, lang=to_lang, slow=False)
        speak.save("output_voice.mp3")

        os.system("start output_voice.mp3 tempo")
