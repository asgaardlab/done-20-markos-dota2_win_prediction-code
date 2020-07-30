# Explainable prediction models for team victory in Dota 2


This repository contains the code and part of the dataset for building and evaluating prediction models for team victory in Dota 2.

You can find the complete dataset [here](http://doi.org/10.5281/zenodo.3890315).

The data was collected from the [OpenDota platform](https://www.opendota.com/)

In this project, we build victory prediction models for Dota 2 and use an interpretability technique ([SHAP values](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf)) to explain the prediction by means of feature importance.


## Directory structure

`data-collection`

The data-collection directory contains the dataset-related code.

* The *hero_changelog* and *hero_historical_stats* directories contain the changelog and attribute values for each Dota 2 hero since Dota 2 first version.

* The identifiers of the matches that compose our dataset can be found in the *match_ids* files (available in csv and json formats), along with additional information.

* The file *opendota-sql-query.txt* contains the SQL query used to retrieve the match ids from the [SQL functionality](https://www.opendota.com/explorer) within the OpenDota platform.

* The file *request_matches.py* reads the match IDs from the csv file (must be in the same directory) and request the match file using the OpenDota API (you must create the output directory in the same directory level as the *request_matches.py* file.  


`data-analysis`

The data-analysis directory contains the data analysis code, inluding the code to build and evaluate the prediction models and the code to apply SHAP values to obtain the predicion explanation by means of feature importance.
