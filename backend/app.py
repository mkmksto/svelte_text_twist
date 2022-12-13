import random
import time
import uuid
from pprint import pprint

from flask import Flask, request
from flask_cors import cross_origin
from utils import dictionary, game_settings

app = Flask(__name__)


class App:
    def __init__(self):
        dict_file_paths = dictionary.get_dict_file_paths()
        all_data = dictionary.get_all_dict_data(dict_file_paths)
        dic_instance = dictionary.RandomWord(all_data)
        self.dict_instance = dic_instance


@app.route('/api')
def index():
    return 'Api Root'


@app.route('/api/random', methods=['GET'])
@cross_origin(origins=['http://127.0.0.1:5173', 'http://localhost:5173'])
def get_random_word():
    rand_word = dict_instance.get_random_word()
    freq = dict_instance.get_frequency(rand_word)
    sub_word = dict_instance.get_subwords(rand_word, max_num=30)
    return {'word': rand_word, 'sub_words': sub_word, 'freq': freq}
    # return {"a": 1, "id": id(rand)}


@app.route('/api/random_word', methods=['POST'])
@cross_origin(
    origins=['http://127.0.0.1:5173', 'http://localhost:5173', 'http://127.0.0.1:5000']
)
def generate_random_word() -> dict:
    """Get a random word and its corresponding subwords
    in python dict format

    This endpoint repeatedly queries for a random word
    until the word actually meets the criteria passed
    by the client through the fetch POST request

    Returns:
        dict: {'word': random_word, 'sub_words': sub_words}
    """

    params: dict = request.json
    pprint(params)
    min_chars = params.get('min_chars', 6)
    max_chars = params.get('max_chars', 12)
    diff: str = params.get('difficulty', 'medium')
    diff: int = game_settings.diff_map.get(diff)
    max_subwords = params.get('max_subwords', 20)

    while True:
        rand_word = dict_instance.get_random_word()
        frequency = dict_instance.get_frequency(rand_word)
        print(rand_word)
        if (
            len(rand_word) < max_chars
            and len(rand_word) > min_chars
            and frequency > diff
        ):
            break

    sub_words = dict_instance.get_subwords(rand_word, max_num=max_subwords)

    shuffled_word = list(rand_word)
    # shuffled_word = [[letter, idx] for idx, letter in enumerate(shuffled_word)]
    shuffled_word = [
        {'letter': letter, 'id': str(uuid.uuid4())} for letter in shuffled_word
    ]
    random.shuffle(shuffled_word)
    # shuffled_word = ''.join(shuffled_word)
    print(shuffled_word)

    return {'word': rand_word, 'sub_words': sub_words, 'shuffled_word': shuffled_word}


if __name__ == '__main__':
    dict_instance = App().dict_instance
    app.run(debug=True)
