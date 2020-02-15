# DATABASE CLEANUP
## Need nltk installed
Download the songs_dataset.csv from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv and store it in your project's home directory then run the
following commands to install a needed library and create a new clean dataset:

**This works for python 3.\*, since 2.\* is no longer supported but should also work on there, just change the Makefile to use 'python' instead of 'python3', and use 'pip' instead of 'pip3'**

'''

pip3 install nltk progress pandas

make db_cleanup

'''

This will take a few hours lol