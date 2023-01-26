#Install packages
from datetime import date, datetime
import os
import math

#3rd party packages
import matplotlib.pyplot as plt
import pandas as pd


dir_path = os.path.abspath("")  # set file path so we can find files in the class folder
pd.set_option("display.max_rows", None)


# First we import some data as a csv and look at it
data_path = os.path.join(dir_path, "../data/W1-2_pump_mwos.csv")
df_pump = pd.read_csv(data_path)
print(df_pump)