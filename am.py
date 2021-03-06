#%%
import os
import tarfile
from six.moves import urllib
#%%
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
#%%
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")

    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# %%
import pandas as pd
# %%
def load_housing_data(housing=HOUSING_PATH):
    csv_path = os.path.join(housing, "housing.csv")
    return pd.read_csv(csv_path)

# %%
housing = load_housing_data()
housing.head()
housing.info()

# %%
housing["ocean_proximity"].value_counts()

# %%
housing.describe()
# %%
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
plt.show()
# %%
import numpy as np

def split_train_test(data, test_ratio):
    # array
    shuffled_indices = np.random.permutation(len(data))
    # Tamanho do conjunto de test
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
# %%
train_set, test_set = split_train_test(housing, 0.2)
# %%
print(len(train_set), "train +", len(test_set), "test")
# %%
