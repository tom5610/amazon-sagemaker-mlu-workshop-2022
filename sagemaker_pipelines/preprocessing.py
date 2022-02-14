
import argparse
import os
import warnings

import pandas as pd
import numpy as np

def do_preprocessing():
    data = pd.read_csv('/opt/ml/processing/input/bank-additional-full.csv')

    # feature engineering
    data['no_previous_contact'] = np.where(data['pdays'] == 999, 1, 0)                                 # Indicator variable to capture when pdays takes a value of 999
    data['not_working'] = np.where(np.in1d(data['job'], ['student', 'retired', 'unemployed']), 1, 0)   # Indicator for individuals not actively employed
    model_data = pd.get_dummies(data)                                                                  

    # drop irrelevant data
    model_data = model_data.drop(['duration', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed'], axis=1)
    
    # split train / validation / test data for training and testing
    train_data, validation_data, test_data = np.split(model_data.sample(frac=1, random_state=1729), [int(0.7 * len(model_data)), int(0.9 * len(model_data))])   # Randomly sort the data then split out first 70%, second 20%, and last 10%
    
    # output data set to local
    train_features_output_path = os.path.join('/opt/ml/processing/output/train', 'train.csv')
    validation_features_output_path = os.path.join('/opt/ml/processing/output/validation', 'validation.csv')
    test_features_output_path = os.path.join('/opt/ml/processing/output/test', 'test.csv')

    pd.concat([train_data['y_yes'], train_data.drop(['y_no', 'y_yes'], axis=1)], axis=1).to_csv(train_features_output_path, index=False, header=False)
    pd.concat([validation_data['y_yes'], validation_data.drop(['y_no', 'y_yes'], axis=1)], axis=1).to_csv(validation_features_output_path, index=False, header=False)
    # keep test data with headers so that we can evaluate model performance with holdout data set.
    pd.concat([test_data['y_yes'], test_data.drop(['y_no', 'y_yes'], axis=1)], axis=1).to_csv(test_features_output_path, index=False, header=False)

if __name__=='__main__':
    
    do_preprocessing()   
    
    print("################# Completed the job in the preprocessing container. #################")
