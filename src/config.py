""" This file is to define the location for model and other configuration """

import os

pathOrg = os.path.abspath(os.path.join(os.path.dirname(__file__), "./..")).replace(
    "\\", "/"
)

model_path = pathOrg + "/model/"

config_path = pathOrg + "/config/"

default_corpus = pathOrg + "/db/"

corpus_name = "big.txt"

model_name = "models_compressed.pkl"

prediction_support = 2
