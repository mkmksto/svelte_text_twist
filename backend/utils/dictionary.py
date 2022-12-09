import glob
import json
import os
import random
from itertools import permutations

import requests


class RandomWord:
    """
    Get a random word with its associated information
    from a dictionary file

    Args:
        data: Dictionary of English dict data
    """

    def __init__(self, data: dict) -> None:
        self.data = data
        self.keys = list(data.keys())

    def get_random_word(self) -> str:
        return random.choice(self.keys)

    def get_rand_word_and_freq(self) -> dict:
        """Get a random word and its corresponding frequency

        Returns:
            dict: {"word": food, "freq": 220.0.1}
        """
        word = random.choice(self.keys)
        freq = self.get_frequency(word)
        return {"word": word, "freq": freq}

    def get_definition(self, word: str) -> dict:
        return self.data.get(word)

    def get_part_of_speech(self, word: str) -> str or None:
        defn: dict = self.get_definition(word)
        meanings: dict = defn.get("MEANINGS", None)
        if meanings:
            meaning_keys = meanings.keys()
            first_key = list(meaning_keys)[0]

        if first_key:
            return meanings.get(first_key)[0]

        return None

    def get_frequency(self, word) -> str:
        data_muse = f"https://api.datamuse.com/words?sp={word}&qe=sp&md=fr&max=1"
        res = requests.get(data_muse, timeout=5)
        if res:
            res = res.json()
            res = res[0]
            res = res.get("tags", None)
            res: str = res[-1]
            res = float(res.split(":")[-1])
            return res
        else:
            return None

    def get_subwords(self, word) -> list:
        site = f"https://www.degraeve.com/subwords.php?w={word}"
        resp = requests.get(site, timeout=5)
        if resp:
            resp = resp.json()

    # @property
    # def permutations(self):
    #     return permutations(self.word)


def get_dict_file_paths(debug=False) -> list:
    """Return the file paths of all the dictionary files

    Returns:
        list: List of file paths
    """

    if debug:
        return glob.glob(os.path.join("..", "dictionary_files/D*.json"))
    return glob.glob("dictionary_files/D*.json")


def get_random_dict_path(file_paths: str) -> str:
    return random.choice(file_paths)


def dict_path_to_dict_data(file_path: str) -> dict:
    """
    Get the data (in dict format) of a random json file

    Returns:
        dictionary:
    """
    with open(file_path, "r", encoding="utf8") as fh:
        dict_data = json.load(fh)

    return dict_data


def get_all_dict_data(file_paths: str) -> dict:
    consolidated_dict = dict()
    for path in file_paths:
        with open(path, "r", encoding="utf8") as fh:
            data: dict = json.load(fh)
            consolidated_dict = consolidated_dict | data

    return consolidated_dict


if __name__ == "__main__":
    dict_file_paths = get_dict_file_paths(debug=True)
    # rand_path = get_random_dict_path(dict_file_paths)
    # rand_dict = dict_path_to_dict_data(rand_path)
    # d = RandomWord(rand_dict)
    # print(d.word)
    # print(d.part_of_speech)
    # print(d.frequency)
    # print(len(list(d.permutations)))

    all_data = get_all_dict_data(dict_file_paths)
    rand = RandomWord(all_data)
    print(rand.get_rand_word_and_freq())
