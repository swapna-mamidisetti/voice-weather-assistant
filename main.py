from VoiceToText import VoiceToText
from TextToVoice import text_to_voice
from weather import get_weather

def main():
    text_to_voice("Please say the city name")
    city = VoiceToText()
    print("City:", city)

    if not city:
        text_to_voice("Sorry, I could not understand")
        return

    result = get_weather(city)
    if not result:
        text_to_voice("City not found")
        return

    print("Weather:", result)
    text_to_voice(result)

if __name__ == "__main__":
    main()