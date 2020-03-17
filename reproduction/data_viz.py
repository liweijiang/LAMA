# Filename: data_viz.py
# Author: Liwei Jiang
# Description: Visualize the data results
# Date: 02/25/2020


import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')

# def bar_plot(data):
