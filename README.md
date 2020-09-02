# Explainable prediction models for team victory in Dota 2

<a href="https://markosviggiato.github.io/" target="_blank"><img src="https://markosviggiato.github.io/img/portfolio/my_website/xai_dota2.png" alt="Explainable AI for Dota 2" title="Explainable AI for Dota 2" width=300 height=175></a>

This repository contains the code and the dataset for building and evaluating prediction models for team victory in Dota 2.

### Dataset
The data was collected from the [OpenDota platform](https://www.opendota.com/) and you can find the used dataset here: </br> <a href="http://doi.org/10.5281/zenodo.3890315" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/8/86/Database-icon.svg" alt="Dota 2 dataset" title="Dota 2 dataset" width=25 height=25></a>

### Explainable prediction model
In this project, we build victory prediction models for Dota 2 and use an interpretability technique ([SHAP values](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf)) to explain the prediction by means of feature importance.

### Paper
For more details on how we collected the data and extracted the model features, please check our Dota 2 paper accepted at the 16th AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE 2020):</br> 
<a href="https://markosviggiato.github.io/resources/Markos_AIIDE_20.pdf" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/8/87/PDF_file_icon.svg" alt="Dota 2 paper" title="Dota 2 paper" width=25 height=25></a>

## Dependencies

The following dependencies are required to run the scripts of this project:

 - Python 3.7
 
 
 - Git 2.20.1.windows.1
  
  
 - [Numpy 1.18.4](https://numpy.org/)

    `
    pip install numpy
    `


 - [Pandas 0.24.2](https://pandas.pydata.org/)
 
    `
    pip install pandas
    `
 
 
 - [scikit-learn 0.20.3](https://scikit-learn.org/stable/)

    `
    pip install scikit-learn
    `


 - [xgboost 1.1.0](https://xgboost.readthedocs.io/en/latest/)

    `
    pip install xgboost
    `
  
  
 - [matplotlib 3.0.2](https://matplotlib.org/)

    `
    pip install matplotlib
    `
    
    
 - [shap 0.35.0](https://github.com/slundberg/shap)

    `
    pip install shap
    `

## Directory structure

`data-collection`

The data-collection directory contains the dataset-related code.

* The *hero_changelog* and *hero_historical_stats* directories contain the changelog and attribute values for each Dota 2 hero since Dota 2 first version.

* The identifiers of the matches that compose our dataset can be found in the *match_ids* files (available in csv and json formats), along with additional information.

* The file *opendota-sql-query.txt* contains the SQL query used to retrieve the match ids from the [SQL functionality](https://www.opendota.com/explorer) within the OpenDota platform.

* The file *request_matches.py* reads the match IDs from the csv file (must be in the same directory) and request the match file using the OpenDota API (you must create the output directory in the same directory level as the *request_matches.py* file.  


`data-analysis`

The data-analysis directory contains the data analysis-related code, including the code to build and evaluate the prediction models and the code to apply SHAP values to obtain the predicion explanation by means of feature importance.

* The file *feature_engineering.ipynb* contains the code to compute the machine learning model features.

* The *hero-attributes* directory contains the script to collect the changelog for all (current) Dota 2 heroes and parse them to extract heroes' attributes for all the game versions.

* The [prediction-models](data-analysis/prediction-models/) directory contains instructions on how to run the code to build and evaluate the prediction models (XGBoost, Random Forest, and Logistic Regression) for team victory in Dota 2.

* The [prediction-explanation-SHAP](data-analysis/prediction-explanation-SHAP/) directory contains instructions on how to run the script to apply the SHAP values technique to explain victory predictions for Dota 2 matches.

Note that the code within the *prediction-models* and *prediction-explanation-SHAP* directories only depend on the computed features, which are readily-available in the [model_features_pre-match](data-analysis/prediction-models/model_features_pre-match/) directory.


## General Questions

If you have any question or suggestion, please contact the repository developer at markosviggiato[at]gmail.com


[https://markosviggiato.github.io/](https://markosviggiato.github.io/)
