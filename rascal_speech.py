import speech_recognition as sr
from translate import Translator

def speech_recognizer_function(language = "hindi", language_code = "hi_EN", energy_threshold = 5000, device_index=1):
    """
    This function captures audio and returns the text

    There are two languages - one specified by the user and one is english

    Output is a tuple with both words. If user chooses English, then its a single value

    Reference/Source: https://realpython.com/python-speech-recognition/#working-with-microphones
    """
    r=sr.Recognizer()

    mic=sr.Microphone(device_index=device_index)

    r.energy_threshold=energy_threshold

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(f"Record your response in {language} now")
        audio=r.listen(source)

    text=r.recognize_google(audio, language = language_code)

    entered_text = text

    if(language == "english"):
        return(entered_text)
    else:
        translator= Translator(from_lang=language, to_lang="english")
        translation = translator.translate(entered_text)
        return(entered_text,translation)

def speech_recognizer_english_us_demo(language = "english", language_code = "en_US", energy_threshold = 5000, device_index=1):
    """
    This function captures audio and returns the text

    There are two languages - one specified by the user and one is english

    Output is a tuple with both words. If user chooses English, then its a single value

    Reference/Source: https://realpython.com/python-speech-recognition/#working-with-microphones
    """
    r=sr.Recognizer()

    mic=sr.Microphone(device_index=device_index)
    audiofile = sr.AudioFile('cinnamon_bun_us.wav')
    with audiofile as source:
        audio = r.record(audiofile)

    r.energy_threshold=energy_threshold

    text=r.recognize_google(audio, language = language_code)

    entered_text = text

    if(language == "english"):
        return(entered_text)
    else:
        translator= Translator(from_lang=language, to_lang="english")
        translation = translator.translate(entered_text)
        return(entered_text,translation)

def speech_recognizer_english_uk_demo(language = "english", language_code = "en_US", energy_threshold = 5000, device_index=1):
    """
    This function captures audio and returns the text

    There are two languages - one specified by the user and one is english

    Output is a tuple with both words. If user chooses English, then its a single value

    Reference/Source: https://realpython.com/python-speech-recognition/#working-with-microphones
    """
    r=sr.Recognizer()

    mic=sr.Microphone(device_index=device_index)
    audiofile = sr.AudioFile('cinnamon_bun_uk.wav')
    with audiofile as source:
        audio = r.record(audiofile)

    r.energy_threshold=energy_threshold

    text=r.recognize_google(audio, language = language_code)

    entered_text = text

    if(language == "english"):
        return(entered_text)
    else:
        translator= Translator(from_lang=language, to_lang="english")
        translation = translator.translate(entered_text)
        return(entered_text,translation)

def speech_recognizer_english_ca_demo(language = "english", language_code = "en_CA", energy_threshold = 5000, device_index=1):
    """
    This function captures audio and returns the text

    There are two languages - one specified by the user and one is english

    Output is a tuple with both words. If user chooses English, then its a single value

    Reference/Source: https://realpython.com/python-speech-recognition/#working-with-microphones
    """
    r=sr.Recognizer()

    mic=sr.Microphone(device_index=device_index)
    audiofile = sr.AudioFile('pasta_canadian.wav')
    with audiofile as source:
        audio = r.record(audiofile)

    r.energy_threshold=energy_threshold

    text=r.recognize_google(audio, language = language_code)

    entered_text = text

    if(language == "english"):
        return(entered_text)
    else:
        translator= Translator(from_lang=language, to_lang="english")
        translation = translator.translate(entered_text)
        return(entered_text,translation)


def rascal_calorie_entry(language = "hindi", language_code="hi_IN"):
    """
    Function for calorie intake entry
    Calls the speech recognizer function and gets output as a tuple in user selected language and english
    """
    print("What did you take?")
    return(speech_recognizer_function(language = language, language_code=language_code))

def rascal_calorie_entry_demo_us(language = "english", language_code="en_US"):
    """
    Function for calorie intake entry
    Calls the speech recognizer function and gets output as a tuple in user selected language and english
    """
    print("What did you take?")
    return(speech_recognizer_english_us_demo(language = language, language_code=language_code))

def rascal_calorie_entry_demo_uk(language = "english", language_code="en_GB"):
    """
    Function for calorie intake entry
    Calls the speech recognizer function and gets output as a tuple in user selected language and english
    """
    print("What did you take?")
    return(speech_recognizer_english_uk_demo(language = language, language_code=language_code))

def rascal_calorie_entry_demo_ca(language = "english", language_code="en_CA"):
    """
    Function for calorie intake entry
    Calls the speech recognizer function and gets output as a tuple in user selected language and english
    """
    print("What did you take?")
    return(speech_recognizer_english_ca_demo(language = language, language_code=language_code))
