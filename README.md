# Rossman Kaggle Mini-Competition

The following project was completed as part of the following [Kaggle Competion](https://www.kaggle.com/competitions/rossmann-store-sales?rvi=1)

The goal was to develop a time-series model to predict the daily sales for 1,115 Rossman stores located across Germany. Rossman is a major drug store that operates in Europe.


Teamname: " #1 "

The python version of our environment is 3.9.7

Follow the instructions below to get started

## Conda environment

To set up the conda environment and dowload the requirements enter these commands:

`conda create --name minicomp python=3.9.7`

`conda config --append channels conda-forge`

`conda activate minicomp`

`pip install -r requirements.txt`

## Python Notebook

After installing sucessfully all the requirments,open the notebook `Compute_RMSPE.ipynb` and go through the different sections.

#### 1 - Data Preparation

By running this cell, an `input_file` is requested from the user, which will be used as the holdout or test file.

In this section we also go over the necessary modifications to prepare the data for our model.

And so this is the transform part of our data pipeline. 

The transformations were made based on our data exploration as we went through feature selection, fixing missing data, removing problematic features with many nulls, and other statistical analysis such as target correlation. 

We also use categorical encoders to turn non numerical features into numbers. In general we used `one_hot_encoder` for most features, however we found that using a `target_encoder` for  store considerably improves the accuracy of our model.



#### 2 - XGB Model

The model chosen is `XGBRegressor` using the `XGBoost` module which is a scalable distributed gradient boosted decision tree model.

The hyperparameters were chosen based on the optimal configuration found during our hyperparameters tunning experiments

Run this cell to train the model using the `fit` function, and get the RMSPE (Root mean square percentage error) for the `input_file`


#### 3 - Formatting Results

Once the predictions are made we just need to do some formatting to fit the `sample_submission.csv` structure and write out the results.


#### 4 - Error Analysis

To improve the performance of our model it is crucial to visualize the results and do some error analysis.

Some data visualization techniques will be needed to isolate, observe and manage erroneous predictions.



# Data

All the data can be found in the corresponding `data` folder

* `store.csv` the data for the 1115 Stores,
* `train.csv` the training dataset
* `test.csv` is the Kaggle competition test dataset
* `holdout_b29.csv` is the DSR mini-competion's test dataset



