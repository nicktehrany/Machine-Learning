# This script cleans up the dataset we retrieved from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv
# by removing unneeded columns, and removing songs that are not in English
# 
# TODO: I guess we could also clean up the other columns in here like the genre being 'rap' instead of '[rap]'?
#       could be easier later on but nor sure?

import csv, re, nltk
import pandas as pd
from nltk.corpus import words
from progress.bar import Bar
nltk.download('words')
with open('songs_dataset.csv', 'r') as dataset, open('data/dataset.csv', 'w+') as out:
    csv_writer = csv.writer(out)
    header = True

    # Pandas is only used for the progress bar to get size of dataset
    pd_reader = pd.read_csv('songs_dataset.csv')
    bar = Bar('Cleaning', max = len(pd_reader) + 1)
    for row in csv.reader(dataset):
        bar.next()
        if not header:
            text = row[6]

            # Removes The unused text with [], (), and {} like [Verse 1:] etc..
            row[6] = re.sub(r'.*\[.*]|\(.*\)|\{.*\}', '', text)
            text = row[6]
            split = text.split()

            # Only writes Songs with English Lyrics to new dataset (Doesn't recognize some words
            # in Rap songs therefore testing multiple random words to hopefully recognize one)
            # Encoding since csv.read returns a string and we need bytes in order to check
            # if it's some character besides ascii by decoding it 
            try:
                str.encode(split[1]).decode('ascii')
            except UnicodeDecodeError:
                pass
            else:

                # If Lyrics are less than 6 words the row is also not written to the file (TODO: Change to a more appropiate number. I chose 6 randomly)
                if (len(split) >= 6):
                    try:
                        str.encode(split[6]).decode('ascii')
                    except UnicodeDecodeError:
                        pass
                    else:
                        if (not text in (None, "")) and (split[1] in words.words() or split[6] in words.words()):
                            csv_writer.writerow([row[0], row[2], row[5], row[6], row[7]])

        header = False
    
    bar.finish()
    dataset.close()
    out.close()           