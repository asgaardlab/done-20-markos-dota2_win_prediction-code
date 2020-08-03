## Building and evaluating victory prediction models for Dota 2

This notebook contains instructions on how to run the scripts to build and evaluate prediction models for team victory in Dota 2.

Note that, for reproducibility purposes, you should use the readily-available model features available in this repository (*model_pre_match_features.zip*).

For more details on how we performed the data preparation and extracted the model features, please check our [Dota 2 paper](https://markosviggiato.github.io/resources/Markos_AIIDE_20.pdf).

---

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
    
## Structure of directories
  
The following directories contains the scripts of each used algorithm. Note that, for each algorithm, there are 3 different scripts, one for each data group we adopted in our study: regular matches, time blowout matches, and score blowout matches.

 - 1 - XGBoost: contains the scripts to read the model features, build and evaluate xgboost models
 - 2 - Random Forest: contains the scripts to read the model features, build and evaluate random forest models
 - 3 - Logistic Regression: contains the scripts to read the model features, build and evaluate logistic regression models
 
## Running the scripts
 
In order to run the scripts to build and evaluate the models, you should place the model features (which can be obtained from this zip file: *model_pre_match_features.zip*) at the same level as this instruction notebook. Also note that you should keep the directory structure of the model feature zip file, which contains sub-directories for each data group we used.

That said, feel free to change the location of the model feature directory and sub-directories as long as you properly adjust the references to those locations in the analysis scripts.
