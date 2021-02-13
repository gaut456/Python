import pandas as pd

dataPath="d:/adp_data/mtech/"

,A,B,C
a,1,2,3
b,4,5,6
c,7,8,9

df=pd.read_csv(dataPath+"test.csv")

df
df.columns #columns

df.index

df.shape #shape of the dataframe

df.set_index('unnammed:0') #set the index

