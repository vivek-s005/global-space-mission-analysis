import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from iso3166 import countries
from datetime import datetime, timedelta
data = pd.read_csv('mission_launches.csv')
print(data.isnull().sum())
print(data.duplicated().sum())