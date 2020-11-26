"""
This type ahead model is based on simple conditional probability concepts
"""
# Import libraries
from bottle import route, run, debug
from collections import Counter
from . import utils
from . import model
from . import config

def load():
    """ load default model """
    model.load_models()
    return True

def predict_currword(word, top_n=10):
    """given a word, return top n suggestions based off frequency of words prefixed by said input word"""
    try:
        return [
            (k, v) for k, v in model.WORDS_MODEL.most_common() if k.startswith(word)
        ][:top_n]
    except KeyError:
        raise Exception(
            "Please load predictive models. Run:\
                        \n\tautocomplete.load()"
        )


def predict_currword_given_lastword(first_word, second_word, top_n=10):
    """ given a word, return top n suggestions determined by the frequency of words prefixed by the input GIVEN the occurence of the last word """
    return Counter(
        {
            w: c
            for w, c in model.WORD_TUPLES_MODEL[first_word.lower()].items()
            if w.startswith(second_word.lower())
        }
    ).most_common(top_n)


def predict(first_word, second_word="", top_n=10):
    """given some text, we [r]split last two words (if possible) and call predict_currword or predict_currword_given_lastword to retrive most n probable suggestions.
    """

    try:
        if first_word and second_word:
            return predict_currword_given_lastword(first_word, second_word, top_n=top_n)
        else:
            return predict_currword(first_word, top_n)
    except KeyError:
        raise Exception("Please load predictive models")