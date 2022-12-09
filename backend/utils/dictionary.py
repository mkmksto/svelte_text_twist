import random
from pprint import pprint
import json
import os


class Dictionary:
    def __init__(self) -> None:
        dict_files = os.path.join("..", "dictionary_files/DA.json")
        with open(dict_files, "r", encoding="utf8") as fh:
            self.data: dict = json.load(fh)

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
        pass

    def get_frequency(self):
        pass


if __name__ == "__main__":
    d = Dictionary()
    print(d.get_random_word())
