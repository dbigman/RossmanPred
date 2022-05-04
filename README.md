## Rossman Kaggle Mini-Competition

Teamname: #1

The python version of our environment is 3.9.7

##Conda environment

Execute the following commands in the 'minicomp-rossman' folder:

conda create --name minicomp python=3.9.7
conda config --append channels conda-forge
conda activate minicomp
pip install -r requirements.txt

##Python script

Execute the script 'Compute_RMSPE.ipynb' in jupyter-lab. It will ask for
the address of the holdout csv file and compute the RMSPE value.

##Exploratory analysis and development

Can be found in 'Jakob.ipynb'.

##Data folder

The 'data' folder contains 'train.csv', and 'store.csv', and 
'holdout_b29.csv', as well as the prediction on the holdout in the file
'predict_holdout.csv'. 
