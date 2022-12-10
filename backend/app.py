import time

from flask import Flask
from flask_cors import cross_origin
from utils import dictionary

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


@app.route('/api/random_word', methods=['GET'])
@cross_origin(origins=['http://127.0.0.1:5173', 'http://localhost:5173'])
def get_random_word():
    rand_word = dict_instance.get_random_word()
    freq = dict_instance.get_frequency(rand_word)
    sub_word = dict_instance.get_subwords(rand_word)
    return {'word': rand_word, 'sub_words': sub_word, 'freq': freq}
    # return {"a": 1, "id": id(rand)}


if __name__ == '__main__':
    dict_instance = App().dict_instance
    app.run(debug=True)
