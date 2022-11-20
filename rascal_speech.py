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

def rascal_calorie_entry(language = "hindi", language_code="hi_IN"):
    """
    Function for calorie intake entry
    Calls the speech recognizer function and gets output as a tuple in user selected language and english
    """
    print("What did you take?")
    return(speech_recognizer_function(language = language, language_code=language_code))

