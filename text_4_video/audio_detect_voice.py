import speech_recognition as sr
def detect_voice(lang, audio_file):
    r = sr.Recognizer()
    micro = sr.AudioFile(audio_file)
    
    with micro as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language = lang)
        except:
            text = 'error: no audio detected'
        return text
