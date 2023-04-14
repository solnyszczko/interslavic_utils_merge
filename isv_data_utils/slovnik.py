import pandas as pd
import os
from isv_data_utils.translation_aux import infer_pos
from isv_data_utils.constants import transliteration




# TODO: https://github.com/gorlatoff/Mashina-bot/blob/main/isv_tools.py

LANGS = {
       'en',
       'ru', 'be', 'uk', 'pl', 'cs', 'sk', 'bg',
       'mk', 'sr', 'hr', 'sl', 'cu', 'de', 'nl', 'eo',
}



def download_slovnik(save=True):
    dfs = pd.read_excel(
        io='https://docs.google.com/spreadsheets/d/e/2PACX-1vRsEDDBEt3VXESqAgoQLUYHvsA5yMyujzGViXiamY7-yYrcORhrkEl5g6JZPorvJrgMk6sjUlFNT4Km/pub?output=xlsx',
        engine='openpyxl',
        sheet_name=['words', 'suggestions']
    )
    dfs['words']['id'] = dfs['words']['id'].fillna(0.0).astype(int)
    dfs['words']['pos'] = dfs['words'].partOfSpeech.astype(str).apply(infer_pos)
    if save:
        dfs['words'].to_pickle("slovnik.pkl")
    return dfs

def get_slovnik(save=True):
    if os.path.isfile("slovnik.pkl"):
        print("Found 'slovnik.pkl' file, using it")
        dfs = {"words": pd.read_pickle("slovnik.pkl")}
    else:
        print("Downloading dictionary data from Google Sheets...")
        dfs = download_slovnik()
        if save:
            dfs['words'].to_pickle("slovnik.pkl")
        print("Download is completed succesfully.")
    prepare_slovnik(dfs['words'])
    return dfs



def prepare_slovnik(slovnik):

    for lang in LANGS:
        assert slovnik[slovnik[lang].astype(str).apply(lambda x: "((" in sorted(x))].empty
    import re
    brackets_regex = re.compile(" \(.*\)")
    for lang in LANGS:
        slovnik[lang].str.replace(brackets_regex, "", regex=True).astype(str)
        if lang in transliteration:
            slovnik[lang] = slovnik[lang].apply(transliteration[lang])
        slovnik[lang + "_set"] = slovnik[lang].str.split(", ").apply(lambda x: set(x))
    slovnik['isv'] = slovnik['isv'].str.replace("!", "").str.replace("#", "").str.lower()
    slovnik['type'] = slovnik['type'].astype(str)
