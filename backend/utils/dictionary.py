import glob
import json
import os
import random
from itertools import permutations

import requests
from bs4 import BeautifulSoup


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
        """Get the english Part of speech given a word

        Args:
            word (str):

        Returns:
            str or None:
        """
        defn: dict = self.get_definition(word)
        meanings: dict = defn.get("MEANINGS", None)
        if meanings:
            meaning_keys = meanings.keys()
            first_key = list(meaning_keys)[0]

        if first_key:
            return meanings.get(first_key)[0]

        return None

    def get_frequency(self, word: str) -> float or None:
        """Return the frequency (per million) for
        a particular word

        Args:
            word (str):

        Returns:
            str: 0.1324
        """
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

    def get_subwords(self, word: str, max_num: int = 30) -> list[str] or list:
        """Get the subwords of a particular word

        Args:
            word (str): rainbow

        Returns:
            list[str] or None: [brown, rain, bow, etc..]
        """

        site = f"https://www.degraeve.com/subwords.php?w={word}"
        resp = requests.get(site, timeout=5)
        if resp:
            resp = resp.text
            soup = BeautifulSoup(resp, "html.parser")
            soup = soup.find_all("ul")
            soup = soup[-1]
            soup = soup.find_all("li")
            soup = [s.contents[0] for s in soup]
            if len(soup) >= max_num:
                soup = soup[:max_num]
            return soup

        return []


def get_dict_file_paths(debug: bool = False) -> list:
    """Return the file paths of all the dictionary files

    Args:
        debug (bool):
            if False, opens the files relative to this file
            if True, gets the paths relative to the flask app, app.py

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

    Args:
        file_path (str): path to the JSON file

    Returns:
        dict: Dictionary data as a python dict
    """
    with open(file_path, "r", encoding="utf8") as fh:
        dict_data = json.load(fh)

    return dict_data


def get_all_dict_data(file_paths: list[str]) -> dict:
    """Given a list of file paths, read all the embedded
    JSON info, then combine them and then return

    Args:
        file_paths (list[str]): ['path/1/DA.json', 'path/2/DZ.json,..]

    Returns:
        dict: Consolidated Dictionary as a python dict
    """
    consolidated_dict = dict()
    for path in file_paths:
        with open(path, "r", encoding="utf8") as fh:
            data: dict = json.load(fh)
            consolidated_dict = consolidated_dict | data

    return consolidated_dict


if __name__ == "__main__":
    dict_file_paths = get_dict_file_paths(debug=True)

    all_data = get_all_dict_data(dict_file_paths)
    rand = RandomWord(all_data)
    # print(rand.get_rand_word_and_freq())
    rand_word = rand.get_random_word()
    subword = rand.get_subwords(rand_word)
    print(rand_word)
    print(subword)
