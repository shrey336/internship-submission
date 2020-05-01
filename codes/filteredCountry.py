import pandas as pd


#Reading the input file as pandas data frames
df=pd.read_csv("main.csv")

#Selecting all rows in csv , where column value is 'USA (CA)'
df=df.loc[df['COUNTRY'].str.contains('USA')]

#Printing the sorted dataframe
print(df)

#Writing the sorted csv file as output: filteredCountry.csv
df.to_csv("filteredCountry.csv")
