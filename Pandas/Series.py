import pandas as pd
a=[1,2,3,4,5]

series=pd.Series(a,index=['a', 'b', 'c', 'd', 'e'],dtype="float",name="Pandas Series")
print(series)
print(type(series))


dic={"name":["python","javascript","c++"],"por":[12,25,30],"rank":[2,1,3]}
series1=pd.Series(dic)
print(series1)
print(type(series1))


series2=pd.Series(12 ,index=[1,2,3,4,5,6,7,8])
series3=pd.Series(12 ,index=[1,2,3,4,5])
print(series2+series3)
# print(type(series2))