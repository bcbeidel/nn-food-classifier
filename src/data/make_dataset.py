# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import os
import h5py

from src import file_utilities


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


def get_h5py_dataset(file_name):
    project_root = file_utilities.get_project_root()
    data_root    = os.path.join(project_root, "data", "external", "food-101", "h5") 
    data_path    = os.path.join(data_root, file_name)
    data         = h5py.File(data_path, "r")
    return data


def get_train_data():
    data = get_h5py_dataset("food_c101_n10099_r32x32x3.h5")

    X_train = data["images"][:]
    Y_train = data["category"][:]
    classes = data["category_names"][:]

    return X_train, Y_train, classes


def get_test_data():
    data = get_h5py_dataset("food_test_c101_n1000_r32x32x3.h5")

    X_test = data["images"][:]
    Y_test = data["category"][:]
    classes = data["category_names"][:]

    return X_test, Y_test, classes


def describe_images_dimensions(X):

    n_images     = X.shape[0]
    image_width  = X.shape[1]  
    image_height = X.shape[2]
    n_colors     = X.shape[3]

    print(f'image count: {n_images}')
    print(f'image dimensions: {image_width}px by {image_height}px; {n_colors} colors')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
