import speech_recognition as sr

def VoiceToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")
        try:
            voice = recognizer.listen(source, timeout=8)
            print("Processing your voice...")
            return recognizer.recognize_google(voice).lower()
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            return None

if __name__ == "__main__":
    print(VoiceToText())