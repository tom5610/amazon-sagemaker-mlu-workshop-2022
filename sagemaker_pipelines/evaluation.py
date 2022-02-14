
import json
import os
import tarfile

import pandas as pd

from sklearn.externals import joblib
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score

if __name__=="__main__":
    model_path = os.path.join('/opt/ml/processing/model', 'model.tar.gz')
    print('Extracting model from path: {}'.format(model_path))
    with tarfile.open(model_path) as tar:
        tar.extractall(path='.')
    print('Loading model')
    model = joblib.load('model.joblib')

    logger.debug("Reading test data.")
    test_data_path = os.path.join('/opt/ml/processing/test', 'test.csv')
    test_data = pd.read_csv(test_data_path, index=None, header=None)
    
    logger.debug("Reading test data.")
    y_test = df.iloc[:, 0].values
    df.drop(df.columns[0], axis=1, inplace=True)
    X_test = xgboost.DMatrix(df.values)
    
    logger.info("Performing predictions against test data.")
    predictions = model.predict(X_test)

    print('Creating classification evaluation report')
    report_dict = classification_report(y_test, predictions, output_dict=True)
    report_dict['accuracy'] = accuracy_score(y_test, predictions)
    report_dict['roc_auc'] = roc_auc_score(y_test, predictions)

    print('Classification report:\n{}'.format(report_dict))

    evaluation_output_path = os.path.join('/opt/ml/processing/evaluation', 'evaluation.json')
    print('Saving classification report to {}'.format(evaluation_output_path))

    with open(evaluation_output_path, 'w') as f:
        f.write(json.dumps(report_dict))
