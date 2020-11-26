""" This file contain the code that create model """
# Import dependencies
import os
import collections
import pickle
from . import utils
from . import config

# Variable initialization
WORDS = []
WORD_TUPLES = []
WORDS_MODEL = {}
WORD_TUPLES_MODEL = {}

def train_models(corpus, model_name=config.model_name):
    """ Function to create the model """
    global WORDS
    WORDS = utils.re_split(corpus)
    global WORDS_MODEL
    WORDS_MODEL = collections.Counter(WORDS)
    global WORD_TUPLES
    WORD_TUPLES = list(utils.chunks(WORDS, config.prediction_support))
    global WORD_TUPLES_MODEL
    WORD_TUPLES_MODEL = {first: collections.Counter() for first, second in WORD_TUPLES}
    for tup in WORD_TUPLES:
        try:
            WORD_TUPLES_MODEL[tup[0]].update([tup[1]])
        except:
            pass
    if model_name:

        save_models(os.path.join(config.model_path, model_name))
    else:
        save_models()
    print("Model trained successfully")

def train_bigtxt(bigtxtpath=None):
    """ Function to train a model using default_corpus """
    if bigtxtpath is None:
        bigtxtpath = os.path.join(config.default_corpus, config.corpus_name)
    with open(bigtxtpath, "rb") as bigtxtfile:
        train_models(str(bigtxtfile.read()))
    print(f"Model trained on {config.corpus_name}")

def save_models(path=None):
    """ Function to save a model"""
    if path == None:
        path = os.path.join(config.model_path, config.model_name)
    print(f"Saving the model in {path}")
    pickle.dump(
        {"words_model": WORDS_MODEL, "word_tuples_model": WORD_TUPLES_MODEL},
        open(path, "wb"),
        protocol=2,
    )

def load_models(load_path=None):
    """ Function to load the model"""
    if load_path is None:
        load_path = os.path.join(config.model_path, config.model_name)
    try:
        models = pickle.load(open(load_path, "rb"))
        global WORDS_MODEL
        WORDS_MODEL = models["words_model"]
        global WORD_TUPLES_MODEL
        WORD_TUPLES_MODEL = models["word_tuples_model"]
        print(f"successfully loaded: {config.model_name}")
    except:
        print("Error in opening pickle object. Training on default corpus text.")
        train_bigtxt()
