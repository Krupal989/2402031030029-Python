import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22]
}

df = pd.DataFrame(data)
print("Data Overview:")
print(df.describe())