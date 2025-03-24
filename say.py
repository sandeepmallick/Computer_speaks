import pyttsx3
bol=pyttsx3.init()
a=input("Enter the text you want to convert to speech: ")
bol.say(a)
bol.runAndWait()
