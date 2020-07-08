'''
DATAPANE INTERACTIVE REPORT

pip install datapane

# https://datapane.com/reports/?name=&owned_by_me=on&order=
# Remember to login
# https://towardsdatascience.com/introduction-to-datapane-a-python-library-to-build-interactive-reports-4593fd3cb9c8
'''

import pandas as pd
import altair as alt
import datapane as dp

df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period2=1585222905&interval=1mo&events=history')

chart = alt.Chart(df).encode(
    x='Date:T',
    y='Open'
).mark_line().interactive()

# Once you have the df and the chart, simply use
r = dp.Report(
  dp.Markdown('My simple report'), #add description to the report
  dp.Table(df), #create a table
  dp.Plot(chart) #create a chart
)

# Publish your report. Make sure to have visibility='PUBLIC' if you want to share your report
r.publish(name='stock_report', visibility='PUBLIC')

