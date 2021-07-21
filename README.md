### This repository presents a multi label text classification solution for automated labelling of Law documents

Objective/ Problem Statement:
----
The task is to automate the labeling of judicial opinions contained in law documents.

Given the dataset (about 500MB), we need to build a model that achieves the desired automation. Every document may contain one or more labels. Thus, this is a classic example of multi label text classification problem


This readme.md file gives a step by step guide to reproduce the solution developed

Below is the folder structure for the solution

```bash
├── README.md          - The top-level README for developers using this project 
├── multi_label_classification.ipynb - Notebook that loads src modules to perform entire preprocessing, visualization to modelling
├── config.yaml        - yaml file to specify input/output data and model paths
├── data               - this folder in git repo is empty, but ideally we will have raw data contained in raw folder. After processing, the data will get generated under processed folder
│   ├── processed      - The final, canonical data sets for modeling
│   └── raw            - The original raw data dump
├── models             - Trained and serialized models
├── requirements.txt   - The requirements file for reproducing the analysis environment
├── src                - Source code for use in this project
│   ├── __init__.py    - Makes src a Python module
│   │
│   ├── data           - Scripts to load or preprocess data
│   │   └── generate_dataset.py - script to load and prepare data with tasks such as parsing json into dataframes, geting cum sum distribution of labels, etc
|   |   └── preprocess.py - script to apply text based preprocessing techniques 
│   │
│   ├── models         - Scripts to train models and further use trained models to make
│   │   │                 predictions
│   │   └── build_model.py
│   │
│   └── visualization  - Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
```

Below are the steps required for reproducing this solution:

Step1: Python environment and package installation
- Assuming we have the folder structure in place as per above format, first step is to ensure we have Python environment (>3). 
I have used is 3.8.5 python version for this implementation.

- Ensure all required packages are installed using
##pip install requirements.txt
It is recommended to create virtual environment and then install required packages to ensure this project has its own dependencies regardless of other projects

Step2: Update config file with below details:
- Specify input and output paths for data - under data section of config
- Specify path where models can be exported in a pickle format - under model section

Step3: Open Jupyter notebook: multi_label_classification.ipynb

Step4: Above Jupyter notebook covers below aspects:
   Step by step data load, parsing data, processing, data exploration & visualization. Followed by multi-label classification model training and evaluation

Idea behind using a jupyter notebook is to visualize data exploration phase such as word clouds and frequency distributions. Instead of a jupyter notebook, we could create .py scripts for preprocessing and modelling tasks by copying relevant code snippets from the notebook.

