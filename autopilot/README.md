# Amazon SageMaker Autopilot Lab

Amazon SageMaker Autopilot is a feature-set that automates key tasks of an automatic machine learning (AutoML) process. Autopilot currently supports regression and binary and multiclass classification problem types. It supports tabular data formatted as CSV or Parquet files in which each column contains a feature with a specific data type and each row contains an observation (target value / label). 

## Why SageMaker Autopilot?

To solve tabular data ML problems is non-traivia, potentially organization will need to hire experts, such as data scientists / ML engineers (expensive resources), to work on the problem. Amazon SageMaker Autopilot makes machine learning eaiser and faster and it help you build classification and regression models without deep machine learning knowledge. 


## Lab Guidance

There are three Jupyter notebooks in the lab. We will introduce a tabular data binary classification problem - Bank Direct Marketing and guide you through data preparation, which is to store the training data on S3 directory; provide 2 options on Autopilot experiment job creations: without code through Amazon SageMaker Studio UI and with code using SageMaker Python SDK. 

> For the lab exercise, please execute the data preparation notebook before either of the remainings.

1. [Data Preparation](./01_sagemaker_autopilot_data_preparation.ipynb)
2. Autopilot Experiment

 a. [Using SageMaker Studio UI](./02a_sagemaker_autopilot_experiment_with_studio_ui.ipynb)
 
 b. [Using SageMaker Python SDK](./02b_sagemaker_autopilot_experiment_with_sdk.ipynb)

