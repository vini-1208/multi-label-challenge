*** Exploratory solution for automated labelling of Procedural Postures** 

This readme.md file gives a step by step guide to reproduce the exploratory solution developed

Below is the folder structure for the solution

```bash
├── README.md          <- The top-level README for developers using this project. <br>
├── config.yaml        <- yaml file to specify input/output data and model paths
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- documentation folder 
│
├── models             <- Trained and serialized models
├── notebooks          <- Jupyter notebooks written for exploration
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to load or preprocess data
│   │   └── generate_dataset.py
|   |   └── preprocess.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   └── build_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
```



-Step1: Python environment and package installation
Assuming we have the folder structure in place as per above format, first step is to ensure we have Python environment (>3). 
I have used is 3.8.5 python version for this implementation.

Ensure all required packages are installed using
##pip install requirements.txt
It is recommended to create virtual environment and then install required packages to ensure this project has its own dependencies regardless of other projects

-Step2: Update config file for below:
Under data section of config, specify input and output paths for data 
Under model section, specify path where models can be exported in a pickle format

-Step3: Open Jupyter notebook: Exploratory_analysis.ipynb

-Step4: Above Jupyter notebook covers below aspects:
   Step by step data load, parsing data, processing, data exploration & visualization. Followed by multi-label classification model training and evaluation


