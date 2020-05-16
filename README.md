nn-food-classifier
==============================

Multi-class classification model implementation on [food-101](https://course.fast.ai/datasets) data set from [Bossard, Lukas et al., 2014](https://www.semanticscholar.org/paper/Food-101-Mining-Discriminative-Components-with-Bossard-Guillaumin/8e3f12804882b60ad5f59aad92755c5edb34860e).  The data set is described as follows:

> 101 food categories, with 101,000 images; 250 test images and 750 training images per class. The training images were not cleaned. All images were rescaled to have a maximum side length of 512 pixels.

Learning Objectives
------------

By the end of this project, I will have demonstrated to myself that I am able to:

- Use python to prepare an image data set for model training
- Leverage visualization libraries to explore model performance
- Leverage AWS S3 to store bulk, raw and intermediate data
- Build A Deep Neural Network in [keras](https://keras.io/)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

Project Setup
--------

In order to download the raw data from S3, the following aws-config is expected.

```
# ~/.aws/config
[profile nn-food-classifier]
aws_access_key_id=FAKEKEY
aws_secret_access_key=FAKESECRETKEY
```

Files can then be download from s3 via the MAKE command `make sync_data_from_s3`. Alternatively, the original files can be downloaded from the [fast.ai course page](https://course.fast.ai/datasets).

--------

Resources
--------

- https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
