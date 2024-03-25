import win32com.client as win32

def pronounce_names(names):
    speaker = win32.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak(f"Shoutout to {name}")

name_list = ["Khan", "Niazii", "Tareen"]
pronounce_names(name_list)
