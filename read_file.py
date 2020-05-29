

states = open('all_usa_states.txt', 'r').read().splitlines()

## 'r' <<<< READ
## 'w' <<<< WRITE / OVERWRITE
## 'a' <<<< APPEND / ADD

read()
splitlines()
strip()
close()

from google.colab import files
uploaded = files.upload() 

from urllib.request import urlopen

def get_words(url: str = "https://norvig.com/ngrams/word.list") -> List[str]:
    """Downloads and returns a set of words from the web"""
    response = urlopen(url)
    return response.read().decode("utf-8").split("\n")
