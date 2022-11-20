from flask import Flask
import sys
from time import gmtime, strftime, localtime
from requests_html import HTMLSession
import nest_asyncio
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from translate import Translator

from rascal_finder import *
from rascal_speech import *

food_item = rascal_calorie_entry(language = "hindi", language_code="hi_IN")[1]

Calories_intake = find_calories_intake(food_item)
Output_text = f"Your calorie intake on eating {Calories_intake[1]} at {Calories_intake[0]} is {Calories_intake[2]} Calories."
app = Flask(__name__)
@app.route('/')
def index():
	return (Output_text)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
