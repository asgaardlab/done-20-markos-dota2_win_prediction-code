# Explainable prediction models for team victory in Dota 2

-----------------

This repository contains the code and part of the dataset for building and evaluating prediction models for team victory in Dota 2.

You can find the complete dataset [here](http://doi.org/10.5281/zenodo.3890315).

The data was collected from the [OpenDota platform](https://www.opendota.com/)

-----------------

## Directory structure

`data-collection`

The data-collection directory contains the dataset-related code:

* The identifiers of the matches that compose our dataset can be found in the *match_ids* files (available in csv and json formats), along with additional information.

* The file *opendota-sql-query.txt* contains the SQL query used to retrieve the match ids from the [SQL functionality](https://www.opendota.com/explorer) within the OpenDota platform.

* The file *request_matches.py* reads the match IDs from the csv file (must be in the same directory) and request the match file using the OpenDota API (you must create the output directory in the same directory level as the *request_matches.py* file.  



