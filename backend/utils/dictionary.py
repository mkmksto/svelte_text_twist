import glob
import json
import os
import random
from pprint import pprint


class RandomWord:
    def __init__(self, data: dict) -> None:
        self.data = data

        keys = list(data.keys())
        word = random.choice(keys)
        entry = data.get(word)
        self.word = word

    def get_random_word(self):
        """
        Returns:
            tuple: A random word and its corresponding
            dictionary entry
        """

        keys = list(self.data.keys())
        word = random.choice(keys)
        entry = self.data.get(word)
        return (word, entry)

    def get_pos(self):
        defn_block: dict = self.data.get(self.word)
        meanings: dict = defn_block.get("MEANINGS", None)
        keys = sorted(list(meanings.keys()))
        # print("keys: ", keys)
        if keys:
            print("meanings: ", meanings)
            print("pos: ", meanings.get(keys[0][0][0], None))
            return meanings.get(keys[0][0][0], None)

        return None

    def get_frequency(self):
        pass


def main():
    # load_random_dict()
    pass


def load_random_dict():
    """Get the data (in dict format) of a random json file

    Returns:
        dictionary:
    """
    dict_file_paths = glob.glob(os.path.join("..", "dictionary_files/D*.json"))
    rand_file = random.choice(dict_file_paths)
    with open(rand_file, "r", encoding="utf8") as fh:
        dict_data = json.load(fh)

    return dict_data


if __name__ == "__main__":
    rand_dict = load_random_dict()
    d = RandomWord(rand_dict)
    d.get_pos()
