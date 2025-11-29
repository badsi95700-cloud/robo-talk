from gtts import gTTS
import os

if __name__ == "__main__":
    print("Welcome to Robo Speaker 1.1 Created by Sifat")
    
    while True:
        x = input("What you want to talk me: ")
        if x.lower() == "bye":
            speech = gTTS("Bye Bye Friend", lang="en")
            speech.save("bye.mp3")
            os.system("start bye.mp3")
            break
            
        speech = gTTS(x, lang="en")
        speech.save("output.mp3")
        os.system("start output.mp3")  # Windows-এ কাজ করে
