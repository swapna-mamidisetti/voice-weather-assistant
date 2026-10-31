# Voice Weather Assistant

A simple Python voice assistant. Say a city name and it tells you the current weather out loud.

## How it works

1. The assistant asks for a city name (text to speech).
2. You say the city name (speech to text).
3. It fetches the weather from the OpenWeather API.
4. It reads the result back to you (text to speech).

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Runs the full flow |
| `VoiceToText.py` | Listens to the microphone and converts speech to text |
| `TextToVoice.py` | Converts text to speech using gTTS and plays it with pygame |
| `weather.py` | Gets weather data from the OpenWeather API |

## Requirements

- Python 3.10 or newer
- A working microphone
- An internet connection
- A free API key from [OpenWeather](https://openweathermap.org/api)

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/swapna-mamidisetti/voice-weather-assistant.git
   cd voice-weather-assistant
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

   If PyAudio fails to install on Windows, use:

   ```
   conda install -c conda-forge pyaudio
   ```

3. Set your OpenWeather API key as an environment variable.

   Windows:

   ```
   setx OPENWEATHER_API_KEY "your_api_key"
   ```

   Close and reopen the terminal afterwards.

   macOS / Linux:

   ```
   export OPENWEATHER_API_KEY="your_api_key"
   ```

## Usage

```
python main.py
```

Wait for the prompt, then say a city name clearly in English, for example "Hyderabad".

## Notes

- Speech recognition uses the Google Web Speech API, so it needs internet.
- A new API key can take 1 to 2 hours to activate.
- The `speech.mp3` file is generated on every run and is ignored by git.
- Very small towns may not be found by the OpenWeather geocoding API.

## License

MIT
