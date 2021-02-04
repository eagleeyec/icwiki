# Sar analysis with Python

df = pd.read_csv('cpu.csv', delimiter=';', parse_dates=['timestamp'])
times = pd.DatetimeIndex(df.timestamp)
hours = df.groupby([times.hour])
hours.agg('max')

## Sar analysis tools

* sargraph.github.io
