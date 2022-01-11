import pandas as pd

#path to file
file = "Spotify/data.csv"
#import and preprocess file
df = pd.read_csv(file)

#show number of variables and amount of data
print(f"number of columns: {len(df.columns)}")
print(f"number of rows: {len(df)}")

#show column name
print(f"column names: ")
for var in df.columns:
    print(var, end= ", ")

#show data types
print(f"\ntypes of data:\n{df.dtypes}")
#choose two columns (energy, duration_ms)
print("chosen columns: energy and duration")
    #show unique values
print(f"unique values in energy:")
energy_values = df.energy.unique()
energy_values.sort()
for value in energy_values:
    print(value)

print(f"unique values in duration:")
duration_values = df.duration_ms.unique()
duration_values.sort()
for value in duration_values:
    print(value)

    #show maximum and minimum values
print(f"maximum value in price {energy_values.max()}, minimum value in price {energy_values.min()}")
print(f"maximum value in year {duration_values.max()}, minimum value in year {duration_values.min()}")

    #show media, mediana and standard deviation
print("energy:")
print(f"    media: {df.energy.mean()}")
print(f"    mediana: {df.energy.median()}")
print(f"    deviacion estandar: {df.energy.std()}")

print("duration:")
print(f"    media: {df.duration_ms.mean()}")
print(f"    mediana: {df.duration_ms.median()}")
print(f"    deviacion estandar: {df.duration_ms.std()}")

 
 
