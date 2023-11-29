import numpy as np
import pandas as pd

def metric(a,b):
    diff = 1 - a/b
    result = sqrt(np.dot(diff,diff)/len(diff))
    return result


def my_data_preparation(train_data, store_data):
    #merge training and store data
    all_data = pd.merge(train_data, store_data, how = 'left', on = 'Store')
    #convert 'Date' to datetime format
    all_data['Date'] = pd.to_datetime(train_data['Date'])
    #extract year, month, day of month, and week of year
    all_data['Year'] = all_data['Date'].dt.year
    all_data['Month'] = all_data['Date'].dt.month
    all_data['Day'] = all_data['Date'].dt.day
    all_data['WeekOfYear'] = all_data['Date'].dt.isocalendar().week.astype(np.int64)
    #fix type errors in the 'StateHoliday' column
    all_data['StateHoliday'] = all_data['StateHoliday'].replace(0.0, '0')
    #dummy encode all categorical data
    all_data = pd.get_dummies(all_data, columns = ['StoreType', 'Assortment', 'StateHoliday'])
    #select only columns with numerical data
    all_data = all_data.select_dtypes(include=np.number)
    #drop columns with too many nans and drop the 'Customers' column
    if 'cutomers' in all_data.columns:
        all_data = all_data.drop(columns=['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Promo2SinceWeek', 'Promo2SinceYear', 'Customers'])
    else:
        all_data = all_data.drop(columns=['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Promo2SinceWeek', 'Promo2SinceYear'])
    return all_data
    if 'Id' in all_data.columns:
        all_data = all_data.drop(columns=['Id'])

    return all_data
    
