import dask.dataframe as dd 

df = dd.read_csv('./files/test.csv', parse_dates=['time'])
df = df[df.isAuthenticated == True]
result = df.groupby('user_id').time.max()
result = result.compute()
result