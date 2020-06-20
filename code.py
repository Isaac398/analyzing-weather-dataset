# --------------
# --------------
import numpy as np
import pandas as pd

def categorical(df):
    categorical_var = df.select_dtypes(include='object')
    return categorical_var.columns

def numerical(df):
    numerical_var = df.select_dtypes(include='number')
    return numerical_var.columns

def clear(df,col,val):
    return df[col].value_counts()[val]

def instances_based_condition(df,col1,val1,col2,val2):
    instance = df[(df[col1] > val1) & (df[col2] == val2)]
    return instance
    
def agg_values_ina_month(df,date_col,agg_col,agg):
    df[date_col] = pd.to_datetime(df[date_col],format = "%Y-%m-%d %H:%M:%S")
    pivot_val = pd.pivot_table(df, index = df[date_col].dt.month, values = agg_col, aggfunc = agg)
    return pivot_val

def group_values(df,col1,agg1):
    group = df.groupby(col1).agg(agg1)
    return group

def convert(df,celsius):
    temp = (df[celsius]*9/5)+32
    return temp    

weather = pd.read_csv(path)
weather.head()

print("Categorical variable",categorical(weather))
print("Numerical variable",numerical(weather))    

print("No.of times weather was cloudy",clear(weather,'Weather','Cloudy'))

wind_speed_35_vis_25 = instances_based_condition(weather, 'Wind Spd (km/h)', 35, 'Visibility (km)', 25)
wind_speed_35_vis_25.head()

print("Mean temperature", agg_values_ina_month(weather, 'Date/Time', 'Temp (C)', 'mean'))

mean_weather = group_values(weather, 'Weather', ['mean'])
mean_weather.head()

print(convert(weather, 'Temp (C)'))



