import pandas 
f1 = pandas.read_excel("activity_data.xlsx") 
f2 = pandas.read_excel("data.xlsx")  
f3 = f2[["_source column"]].merge(f1[["hide","rating","watchlist","watched"]],  
                                     on = "_source column",  
                                     how = "left") 
  
f3.to_excel("output.xlsx", index = False)
read_file = pandas.read_excel ("output.xlsx") 
read_file.to_csv ("output.csv",index = None, header=True)
df = pd.DataFrame(pd.read_csv("output.csv")) 
df