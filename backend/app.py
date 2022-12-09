import time

from flask import Flask
from flask_cors import cross_origin
from utils import dictionary

app = Flask(__name__)


class App:
    def __init__(self):
        dict_file_paths = dictionary.get_dict_file_paths()
        all_data = dictionary.get_all_dict_data(dict_file_paths)
        dict_instance = dictionary.RandomWord(all_data)
        self.dict_instance = dict_instance


@app.route("/api")
def index():
    return "Api Root"


@app.route("/api/random_word", methods=["GET"])
def get_random_word():
    return dict_instance.get_rand_word_and_freq()
    # return {"a": 1, "id": id(rand)}


if __name__ == "__main__":
    dict_instance = App().dict_instance
    app.run(debug=True)