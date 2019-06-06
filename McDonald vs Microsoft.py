#!/usr/bin/env python
# coding: utf-8

# In[123]:


#Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import datetime
import quandl
from statsmodels.stats.stattools import durbin_watson
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[124]:


#Dates to fetch data
start = datetime.datetime(2016,1,1)
end = datetime.datetime(2017,1,1)

#API_Key
quandl.ApiConfig.api_key = 'TQUQzkUTBHrerch_9RnN'

#Comparing McDonald and Microsoft
McDonald = quandl.get("EOD/MCD", start_date = start, end_date = end)
Microsoft = quandl.get("EOD/MSFT", start_date = start, end_date = end)

#Sample size
n = len(McDonald)
print('The sample size is ', n, '.')


# In[125]:


#Check that McDonald's data is working
McDonald.head()

#Check the datatype
type(McDonald)


# In[126]:


#Check that Microsoft's data is working
Microsoft.head()

#Check the datatype
type(Microsoft)


# In[127]:


#Slice the close column from both dataframes
MCD = McDonald.iloc[ : , 3]
MSFT = Microsoft.iloc[ : , 3]

#Check columns are sliced
MCD
MSFT


# In[128]:


#Examine the correlation between McDonald and Microsoft
Correlation = np.corrcoef(MCD, MSFT)[0,1]
print('Correlation: ', Correlation)


# In[129]:


plt.scatter(MCD, MSFT, marker = ".")
plt.xlabel('McDonald')
plt.ylabel('Microsoft')


# In[130]:


#Using Spearman rank coefficient
Spearman = stats.spearmanr(MCD, MSFT)

#Spearman rank coefficient returns the coefficient in the first value and p-value in the second value
print('Spearman Rank Coefficient: ', Spearman[0])
print('p-value: ', Spearman[1])

#Using alpha of 0.05 as the cutoff for significance
alpha = 0.05
if Spearman[1] <= alpha:
    print('The result that McDonald and Microsoft are negatively correlated is statistically significant.')
else:
    print('The result that McDonald and Microsoft are negatively correlated is not statistically significant.')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




