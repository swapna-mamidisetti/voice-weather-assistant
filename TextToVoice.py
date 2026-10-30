from gtts import gTTS
import time
import pygame

def text_to_voice(text, lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("speech.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()

if __name__ == "__main__":
    text_to_voice("Hello, how are you?")