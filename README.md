# DATABASE CLEANUP
## Required Packages
Download the songs_dataset.csv from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv and store it in your project's home directory then run the
following commands to install a needed library and create a new clean dataset:

**This works for python 3.\*, since 2.\* is no longer supported but should also work on there, just change the Makefile to use 'python' instead of 'python3', and use 'pip' instead of 'pip3'**

'''

pip3 install nltk tqdm pandas regex

make clean-dataset

'''

This will take a few hours lol

# DATA ANALYSIS
The final train data set will be created in the data folder, in which there's also a jupyter notebook in which data analysis should be done (Graphs
of the distribution, etc..). Jupyter can be used by running the following command in either the project's home folder or the data folder.

'''

jupyter notebook

'''