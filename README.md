# Machine Learning Project

Multiple machine learning model implementations that classify music genres based on the lyrics.

## DATASET CLEANUP AND DATA SPLIT

**Test, Validate, and Train data is included in the repo**

Download the songs_dataset.csv from https://www.kaggle.com/detkov/lyrics-dataset/version/5#songs_dataset.csv and store it in your project's src directory then run the
following commands to install needed libraries and create a new clean dataset:

### Required Packages

**This works for python 3.\*, since 2.\* is no longer supported but should also work on there, just change the Makefile to use 'python' instead of 'python3', and use 'pip' instead of 'pip3'**

```console
pip3 install nltk tqdm pandas regex
make clean-dataset
```

This will take a few hours, therefore ran the script once and included the dataset in the src folder.
The dataset cleaner script is in the util directory and will display several progress bars on the terminal while running.

After running the cleanup script we ran the data split once to create the test, validation, and train data sets, which are all stored in the src folder.

## Models

All models are in the src folder. The Models are:

* Artificial Neural Network
* Convolutional Neural Network
* K-nearest Neighbour
* Logistic Regression
* Naive Bayes

## Helper Functions

To keep the code for the models simple and compact, we placed all our functions (cleaning text, creating one-hot vectors, etc.)
inside a file called helper functions in the util directory. We import this file on begin of the model script and call the functions as
needed.
