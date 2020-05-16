import sys, os, random

import numpy as np
import matplotlib.pyplot as plt

def display_random_image(X, Y, classes):

    n_X = len(X)
    index = random.randint(1, n_X)
    label_assignment = Y[index]
    label_name = classes[label_assignment].item().decode("utf-8")

    print(f"Displaying image at index {index} with label {label_name}")

    plt.imshow(X[index])