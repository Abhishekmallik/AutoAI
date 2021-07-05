def get_libraries():
    ret_str = """import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
%matplotlib inline
import matplotlib.pyplot as plt

import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn

import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import seaborn as sns
init_notebook_mode(connected=True)
import random
import math
import scipy.stats as ss"""

    return ret_str
