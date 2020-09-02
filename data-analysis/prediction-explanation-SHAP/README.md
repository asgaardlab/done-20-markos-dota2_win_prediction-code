## Feature importance to explain victory predictions for Dota 2

This notebook contains instructions on how to run the script to apply the [SHAP values](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf) technique to explain victory predictions for Dota 2 matches. We apply SHAP values to the predictions made by out XGBoost models, which are implemented together with the SHAP technique.

Note that, for reproducibility purposes, you can use the readily-available model features available in the [model_features_pre-match](../../data-analysis/prediction-models/model_features_pre-match/) directory or you can get the *model_pre_match_features.zip* file with the features [here](http://doi.org/10.5281/zenodo.3890315).

For more details on how we performed the data preparation, extracted the model features, and adapted the SHAP technique for our data, please check our [Dota 2 paper](https://markosviggiato.github.io/resources/Markos_AIIDE_20.pdf).

---

## Dependencies

The following dependencies are required to build and evaluate the prediction models:

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
    
## Structure of directories

In this directory, you will find the following sub-directories with corresponding contents:

 - XGBoost: contains the script to read the model features, build and evaluate xgboost models along with the script to apply the SHAP technique to the prediction made by the XGBoost model
 - SHAP_plots: contains the generated SHAP plots (summary plots and barplots)
 
## Running the scripts

 **Important note:** the scripts used in this part of the work were run on [Google colab](https://colab.research.google.com/notebooks/welcome.ipynb), where you do not need to install all the dependencies (only the *shap* library). Note that some steps are slighty different compared to running the scripts on a local machine (e.g., the functions to read the data rely on the data uploaded to the google colab session). If you desire to run the scripts locally on your machine, you need to install the dependencies (link above).

---

In order to run the scripts to build and evaluate the models, you should place the model features (which can be obtained from this zip file: *model_pre_match_features.zip*) at the location you desire. Note that, for the script to read the feature files, you need to set the correct path to the location you chose.

This script contains the XGBoost implementation we used in the paper, which is the model we use to apply the SHAP values.

We perform a grid search to tune the hyperparameters of the XGBoost model. The grid of values that we use can be adjusted to incorporate more values.

Finally, the script to apply the SHAP technique generates two types of plots (summary plots and barplots). Feel free to specify a location to save those plots.

