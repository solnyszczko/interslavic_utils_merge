import sys
import os
PATH = os.path.dirname(sys.argv[0])
sys.path.append("/home/meow/mytest/isv_data_gathering/")
#"home/meow/dev/isv_data_gathering/"
#FIX THIS WEIRD PATH STUFF
from conllu.parser import parse_dict_value
from io import open


import string
from isv_data_utils import constants
from isv_data_utils import translation_aux
from isv_data_utils import isv_translate as it



punctuation_chars = list(string.punctuation)
punctuation_chars.extend(['‘', '’', '“', '”', '…', '–', '—', '„'])

morph = constants.create_analyzers_for_every_alphabet(PATH)['etm']

#postprocess_translation_detailss



from isv_data_utils import constants
from isv_data_utils.slovnik import get_slovnik, prepare_slovnik

dfs = get_slovnik()
slovnik = dfs['words']
prepare_slovnik(slovnik)
#print(slovnik)
etm_morph = constants.create_etm_analyzer(PATH)

sent = "Północna Algieria leży w strefie umiarkowanej i cieszy się łagodnym, śródziemnomorskim klimatem."
lang = "pl"

parsed = it.prepare_parsing(sent, lang)
print(parsed)
udpipe_details = it.translate_sentence(parsed, lang, slovnik, etm_morph)

print(udpipe_details.translation_candidates.values.tolist())

print("".join(x['str'] for x in it.postprocess_translation_details(udpipe_details)))
