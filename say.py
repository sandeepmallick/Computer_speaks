import pyttsx3
bol=pyttsx3.init()
a=input("say something:")
bol.say(a)
bol.runAndWait()