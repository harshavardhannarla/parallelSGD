import pandas as pd
import numpy as np
import csv
import sys
import os
from sklearn import preprocessing
import zipimport
# jar_file, input_file_local, input_dir, output_dir, mapper_dir, reducer_dir = sys.argv[1:]

df = pd.read_csv('data1.csv')


df.reindex(np.random.permutation(df.index))

data = df.values
min_max_scaler = preprocessing.MinMaxScaler()
data_scaled = min_max_scaler.fit_transform(data)
df = pd.DataFrame(data_scaled)
m, n = df.shape
df.reset_index(drop=True, inplace=True)

df.to_csv('data_shuffled1.csv', index=False, header=False)

f = open('input.txt', 'w')
with open('data_shuffled1.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        n = len(row)
        for i in range(n):
            if i == n-1:
                print(row[i], file=f)
            else:
                print(row[i]+',', file=f, end='')
f.close()
