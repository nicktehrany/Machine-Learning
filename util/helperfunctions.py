from tensorflow.keras.utils import to_categorical
import re # for removing special characters
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords # For removing stopwords
import numpy as np
import math


def sigmoid_logit(x):
    if x >= 0.3:
        return 1
    elif x == 0:
        return 0

    numerator = math.e**(math.log(x/(0.3-x)))
    return numerator/(numerator + 1)

# creates a one-hot zero initialized vector of size size
# for the given text from the word_list 
def one_hot(text, wlist, size, type):
    word_vector = np.zeros(shape=(1, size))
    text = text.split() # splits words
    for w in text:
        ind = get_index(w, wlist)
        if ind >= 0:
            if type == 0:
                word_vector[0, ind] = 1
            if type == 1:
                word_vector[0, ind] += 1
    
    temp = word_vector[0]

    # Used for sigmoid-logit term frequency
    # index = 0
    # for x in temp:
    #     temp[index] = sigmoid_logit(x)
    #     index +=1

    return temp


def get_index(word, word_list):
    for index, value in enumerate(word_list):
        if word == value:
            return index
    return -1


# takes a list and creates a one-hot vector for the genre and retruns it as a list
def one_hot_genres(genres):
    one_hot = []

    for value in genres:
        index = 0
        if value == '[\'Pop\']': index = 0
        elif value == '[\'Rock\']': index = 1
        elif value == '[\'Hip-Hop/Rap\']': index = 2
        elif value == '[\'Country\']': index = 3
        elif value == '[\'R&B/Soul\']': index = 4
        elif value == '[\'Metal\']': index = 5
        elif value == '[\'Alternative/Indie\']': index = 6
        elif value == '[\'Folk\']': index = 7
        one_hot.append(index)

    one_hot = to_categorical(one_hot, 8)
    return one_hot

# takes a list and a boolean. cleans the text in the list and if boolean is true,
# creates a list of all words that occured in the text. returns cleaned text as a 
# list and and list of words or empty list
def clean_text(text_list, use_list):
    corpus = []
    sw = stopwords.words("english")
    word_list = []
    for text in text_list:
        text = re.sub('[^a-zA-Z]', ' ', text) # removes special characters
        text = text.lower() # lowercases everything
        text = text.split() # splits words
        text = [wordnet_lemmatizer.lemmatize(word, pos="v") for word in text if not word in set(sw)]
        formatted_text = ""
        for word in text:
            if use_list:
                if word not in word_list:
                    word_list.append(word)
            formatted_text+=word+" "
        corpus.append(formatted_text)
    text_list = corpus

    return (text_list, word_list)

# takes a list and a boolean. cleans the text in the list and if boolean is true,
# creates a list of all words that occured in the text. returns cleaned text as a 
# list, list of words or empty list, and the lentgh of words for the longest text
def cnn_clean_text(text_list, use_list):
    corpus = []
    sw = stopwords.words("english")
    word_list = []
    max_len = 0
    for text in text_list:
        counter = 0
        text = re.sub('[^a-zA-Z]', ' ', text) # removes special characters
        text = re.sub(',', '', text)
        text = text.lower() # lowercases everything
        text = text.split() # splits words
        text = [wordnet_lemmatizer.lemmatize(word, pos="v") for word in text if not word in set(sw)]
        formatted_text = ""
        for word in text:
            counter+=1
            if use_list:
                if word not in word_list:
                    word_list.append(word)
            formatted_text+=word+" "
        corpus.append(formatted_text)
        if counter > max_len:
            max_len = counter
    text_list = corpus

    return (text_list, max_len, word_list)

# reverses the one-hot genres vector back to genres and returns it as a list
def one_hot_reverse(genre_list):
    genres = []

    for i in range(len(genre_list)):
        x = genre_list[i]
        for index in range(0, 8):
            if x[index] == 1.0:
                genres.append(index)

    return genres