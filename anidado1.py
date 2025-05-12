import win32com.client
import time

for i in range (5):
    j = 0
    while j < 5:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        voices = speaker.GetVoices()
        spanish_voice = voices.Item(0)
        speaker.Voice = spanish_voice
        text = "Hola mundo"
        speaker.Speak(text)
        print(text)
        time.sleep(1)
        j += 1
