SHELL = /bin/sh

DS = songs_dataset.csv
CleanDB = data/dataset.csv
ds_clean = util/data_cleaner.py
PY = python3

.PHONY: all clean

clean-dataset:
	mkdir -p data
	$(PY) $(ds_clean) 
	$(RM) $(DS)



