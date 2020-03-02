from tensorflow.keras.utils import to_categorical
import numpy as np

# creates a one-hot zero initialized vector of size size
# for the given text from the word_list 
def one_hot(text, wlist, size):
    word_vector = np.zeros(shape=(1, size))
    text = text.split() # splits words
    for w in text:
        ind = get_index(w, wlist)
        if ind >= 0:
            word_vector[0, ind] = 1
    return word_vector[0]


def get_index(word, word_list):
    for index, value in enumerate(word_list):
        if word == value:
            return index
    return -1
