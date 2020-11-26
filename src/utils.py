""" This file contains all the functions used in the model """

import re


def norm_rsplit(text, n):
    """ Function to make the text to lower case and split it"""
    return text.lower().rsplit(" ", n)[-n:]


def re_split(text):
    """ Function to find the list of words """
    return re.findall("[a-z]+", text.lower())


def chunks(l, n):
    """ Function to make a chunk of words from the long string """
    for i in range(0, len(l) - n + 1):
        yield l[i : i + n]
