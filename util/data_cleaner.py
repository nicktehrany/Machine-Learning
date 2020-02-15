# This script cleans up the dataset we retrieved from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv
# by removing unneeded columns, and removing songs that are not in English
#
# Lyrics will only have one genre to make it simpler
#
# This script will remove unwanted data from the lyrics and select 200 Songs from each genre to be put into the final
# set. This will result in a perfectly even distribution over our training data.
#
#
# TODO: I guess we could also clean up the other columns in here like the genre being 'rap' instead of '[rap]'?
#       could be easier later on but nor sure?

import csv, re, nltk
import pandas as pd
from nltk.corpus import words
import signal
from tqdm import *
nltk.download('words')

# Change Max_songs to a sutiable number for how many songs of each genre should be in the final set
Max_songs = 1800; finished = 0
CONST_POP = '[\'Pop\']'; CONST_ROCK = '[\'Rock\']'; CONST_RAP = '[\'Hip-Hop/Rap\']'; CONST_COUNTRY = '[\'Country\']';
CONST_RB = '[\'R&B/Soul\']'; CONST_METAL = '[\'Metal\']'; CONST_INDIE = '[\'Alternative/Indie\']'; CONST_FOLK = '[\'Folk\']'
counter = [0,0,0,0,0,0,0,0]

def signal_handler(signal, sigframe):
    exit(0)

def update_bar(index):
    if index == 0: pop_bar.update(1) 
    elif index == 1: rock_bar.update(1)
    elif index == 2: rap_bar.update(1)
    elif index == 3: country_bar.update(1)
    elif index == 4: rb_bar.update(1)
    elif index == 5: metal_bar.update(1)
    elif index == 6: indie_bar.update(1)
    elif index == 7: folk_bar.update(1)

def match_genre(row):
    if row == CONST_POP: index = 0
    elif row == CONST_ROCK: index = 1
    elif row == CONST_RAP: index = 2
    elif row == CONST_COUNTRY: index = 3
    elif row == CONST_RB: index = 4
    elif row == CONST_METAL: index = 5
    elif row == CONST_INDIE: index = 6
    elif row == CONST_FOLK: index = 7
    else:
        return 1
    
    if counter[index] >= Max_songs:
        return 1
    counter[index]+=1
    if counter[index] == Max_songs:
        global finished 
        finished+=1
    update_bar(index)
    return 0

def clean_row(row):

    # Removes The unused text inside [], (), and {} like [Verse 1:] etc..
    row[6] = re.sub(r'\[\[*[^]]*\]\]*|\(.[^)]*\)\)*|\{\{*[^}]*\}\}*', '', row[6])
    text = row[6]
    split = text.split()

    # Only writes Songs with English Lyrics to new dataset (Doesn't recognize some words
    # in Rap songs therefore testing multiple random words to hopefully recognize one)
    # Encoding since csv.read returns a string and we need bytes in order to check
    # if it's some character besides ascii by decoding it 
    try:
        if len(split) > 1:
            str.encode(split[1]).decode('ascii')
    except UnicodeDecodeError:
        pass
    else:
        # If Lyrics are less than 6 words the row is also not written to the file (TODO: Change to a more appropiate number. I chose 6 randomly)
        if len(split) > 6:
            try:
                str.encode(split[6]).decode('ascii')
            except UnicodeDecodeError:
                pass
            else:
                if (split[1] in words.words() or split[6] in words.words()):
                    row[5] = re.sub(r',.*\'', '', row[5])
                    success = match_genre(row[5])
                    if finished == 8:
                        return 0
                    if success == 0:
                        csv_writer.writerow([row[0], row[2], row[5], row[6], row[7]])

                        
with open('songs_dataset.csv', 'r') as dataset, open('data/dataset.csv', 'w+') as out:
    csv_writer = csv.writer(out)
    header = True
    signal.signal(signal.SIGINT, signal_handler)

    # Pandas is only used for the progress bar to get size of dataset
    pd_reader = pd.read_csv('songs_dataset.csv')
    cleaning_bar = tqdm(desc = "Searching", total = len(pd_reader) + 1)
    pop_bar = tqdm(desc = "Pop", total = Max_songs)
    rock_bar = tqdm(desc = "Rock", total = Max_songs)
    rap_bar = tqdm(desc = "Hip-Hop/Rap", total = Max_songs)
    country_bar = tqdm(desc = "Country", total = Max_songs)
    rb_bar = tqdm(desc = "R&B", total = Max_songs)
    metal_bar = tqdm(desc = "Metal", total = Max_songs)
    indie_bar = tqdm(desc = "Indie", total = Max_songs)
    folk_bar = tqdm(desc = "Folk", total = Max_songs)
    for row in csv.reader(dataset):
        if not header:
            prog = clean_row(row)
            if prog == 0: break
        else:
            csv_writer.writerow([row[0], row[2], row[5], row[6], row[7]])
        cleaning_bar.update(1)
        header = False
    
    dataset.close()
    out.close()
