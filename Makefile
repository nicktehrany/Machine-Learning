SHELL = /bin/sh

DS = songs_dataset.csv
ds_clean = util/data_cleaner.py
PY = python3

.PHONY: all clean

all: clean-dataset

clean-dataset:
	mkdir -p src
	$(PY) $(ds_clean) 
	
clean:
	$(RM) $(DS)

