from flask import Blueprint
import os
from dotenv import load_dotenv
import requests
import random

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

word_key = os.environ.get("WORD_KEY")
art_key = os.environ.get("ART_KEY")

@proxy_bp.route("/word", methods=("GET",))
def get_random_word():
    response = requests.get(
        "http://api.wordnik.com/v4/words.json/randomWord",
        params={"api_key": word_key, "hasdictionarydef": "true", "excludepartofspeech": "adverb,interjection,pronoun,preposition,abbreviation,affix,article,auxiliary-verb,conjunction,definite-article,family-name,given-name,idiom,imperative,noun-plural,noun-posessive,past-participle,phrasal-prefix,proper-noun,proper-noun-plural,proper-noun-posessive,suffix,verb-intransitive,verb-transitive", "mindictionarycount": "10000" }
    )

    return response.json()

@proxy_bp.route("/art", methods=["GET"])
def get_art():
    response = requests.get(
        "https://www.rijksmuseum.nl/api/en/collection",
        params={"key": art_key, "ps": "100", "p": random.randrange(0,99), "imgonly": "true", }
    )
    return response.json()