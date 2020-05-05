from collections import deque
import spacy as sp
import numpy as np
import pandas as pd

"""
    Utilities to work with text files for NLP tasks.
"""

# Operations on text corpora
class Corpus:

    def __init__(self):
        pass


    # Magic function, adding multiple corpora together
    def __add__(self):
        pass



# High-level interface for NLP-Taks
class NLP:

    def __init__(self, corpus):
        self.corpus = corpus



# Returns tokens
def tokenize(corpus, lemmatize=False):

    if not isinstance(corpus, str):
        raise ArgumentError("Error in tokenize/1. Expected a String corpus, got something else.")

    nlp = sp.load("en_core_web_sm") # load language model
    doc = nlp(corpus)

    if lemmatize:
        return np.array([token.lemma_ for token in doc])
    else:
        return np.array([token.text for token in doc])


# REVIEW: DataFrame or dictionary?
# Expects vector as input
# returns encoding table for tokens
def one_hot_encode(tokens):
    unique_tokens = np.unique(tokens)
    vec_length, = unique_tokens.shape
    zeros = np.zeros(vec_length)
    
    lookup_build = deque()
    for index in range(vec_length):
        token = unique_tokens[index]    
        
        # Copy vector and set one-hot-value
        one_hot_vector = zeros.copy()
        one_hot_vector[index] = 1

        lookup_build.appendleft([token, one_hot_vector])

    return dict(list(lookup_build))


# Return a dataframe with word frequencies
def word_frequency(corpus_or_):
    pass


