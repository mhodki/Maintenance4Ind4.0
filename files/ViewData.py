#Install packages
from datetime import date, datetime
import os
import math

#3rd party packages
import matplotlib.pyplot as plt
import pandas as pd


dir_path = os.path.abspath("")  # set file path so we can find files in the class folder
pd.set_option("display.max_rows", None)


# An extract of some key columns in an IW39 maintenance word order report for a single pump over its life
data_path = os.path.join(dir_path, "../data/W1-2_pump_mwos.csv")
df_pump = pd.read_csv(data_path)
print(df_pump)

# An extract of some key columns in an maintenance word order report for an excavator over its life
data_path = os.path.join(dir_path, "../data/Excavator_2015_Raw_ForPDL.csv")
df_excv = pd.read_csv(data_path)
print(df_excv)

# An extract of some condition monitoring oil analysis for a set of engines
data_path = os.path.join(dir_path, "../data/engine_anon.csv")
df_engoil = pd.read_csv(data_path)
print(df_engoil)


