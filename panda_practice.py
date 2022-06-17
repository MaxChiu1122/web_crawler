import pandas as pd
data = pd.Series([20,10,15])
#print(data)
# print('Max', data.max())
# print('Median', data.median())
# data = data*2
# data=data==20
# print(data)
data = pd.DataFrame({
    'name':['Amy','John','Bob'],
    'salary':[30000,50000,20000]
})
#print(data)
#print(data['salary'])
print(data.iloc[0])