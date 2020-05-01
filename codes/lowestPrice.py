import pandas as pd
import csv 


#Reading the input file as pandas data frames
df=pd.read_csv("filteredCountry.csv")
print(df)

df=df[['SKU', 'PRICE']]
print(df)

sku = list(df['SKU'])
price = list(df['PRICE'])

chk = 0
cnt = 0
cll = 0
min1 = 0
min2 = 0

skulist = list()
min1list = list()
min2list = list()

for i in sku:
    if chk != i:
        if cll >= 2:
            skulist.append(chk)
            min1list.append(min1)
            min2list.append(min2)
            min1 = 0
            min2 = 0
        chk = i
        min1 = price[cnt]
        cll = 1
    elif chk == i and cll == 1:
        cll = cll+1
        if min1 >= price[cnt]:
            min2 = min1
            min1 = price[cnt]
        else:
            min2 = price[cnt]
    elif chk == i and cll >= 2:
        cll = cll+1
        if min1 > price[cnt]:
            min2 = min1
            min1 = price[cnt]
        elif min2 > price[cnt]:
            min2 = price[cnt]
    cnt = cnt+1

l = len(skulist)


tex = [0,0,0]


    
    
lp = "lowestPrice.csv"

fields = ["SKU", "FIRST_MINIMUM_PRICE", "SECOND_MINIMUM_PRICE"]




with open(lp, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in range(l):
        tex[0] = skulist[i]
        tex[1] = min1list[i]
        tex[2] = min2list[i]
        csvwriter.writerow(tex)
    
    
    
    
    
    
    

        
            
            

        
        
        
        
    
    




