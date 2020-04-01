import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['month'] = pd.to_datetime(df['date'])

# Preparing data
trace1 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Maximum')
trace2 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='Mean')
trace3 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='Minimum')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Actual Maximum, Minimum, and Mean Temperatures by Month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilineweather.html')