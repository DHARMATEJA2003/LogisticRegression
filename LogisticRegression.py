#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# %%
data=pd.read_csv("C:/Users/91901/Documents/LogisData.csv")
data#"C:\Users\91901\Documents\LogisData.csv"
#%%
X,Y=data["age"],data["insurance"]
# %%
import sklearn
from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2,random_state=20)
# %%
Xtrain,Ytrain

#%%
plt.scatter(Xtrain,Ytrain)
# %%
from sklearn.linear_model import LogisticRegression
# %%
lr=LogisticRegression()
# %%
xtrain=np.array(Xtrain).reshape(-1,1)
ytrain=np.array(Ytrain).reshape(-1,1)
xtest=np.array(Xtest).reshape(-1,1)
# %%
lr.fit(xtrain,ytrain)
# %%
xtest=np.array(xtest).reshape(-1,1)
lr.predict(xtest)
#%%
