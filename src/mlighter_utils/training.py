from sklearn.model_selection import train_test_split
import pandas as pd

from . import constants

# Default data set for testing
IRIS_DATASET_URL = constants.PATH_TO_DATASETS + "iris.csv"
IRIS_FLOWER_NAMES = names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']


def get_default_dataset() -> pd.DataFrame:
    return pd.read_csv(IRIS_DATASET_URL, names=IRIS_FLOWER_NAMES)


def extract_xy_train(dataset: pd.DataFrame, test_size: int = 0.20, random_state=constants.FIXED_RANDOM_VALUE) \
        -> (pd.DataFrame, pd.DataFrame):
    array = dataset.values
    x = array[:, 0:4]
    y = array[:, 4]

    x_train, _, y_train, _ = train_test_split(x, y, test_size=test_size, random_state=random_state)

    return x_train, y_train
