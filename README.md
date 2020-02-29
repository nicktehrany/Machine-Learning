# DATASET CLEANUP
## Required Packages
Download the songs_dataset.csv from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv and store it in your project's home directory then run the
following commands to install needed libraries and create a new clean dataset:

**This works for python 3.\*, since 2.\* is no longer supported but should also work on there, just change the Makefile to use 'python' instead of 'python3', and use 'pip' instead of 'pip3'**

```console
pip3 install nltk tqdm pandas regex
make clean-dataset
```

This will take a few hours, therefore ran the script once and included the dataset in the src folder.

# Models
All models are in the src folder. (TODO: Describe different Models)