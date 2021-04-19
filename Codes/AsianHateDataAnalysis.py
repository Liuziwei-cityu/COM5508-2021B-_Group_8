#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt 

data = pd.read_csv('before.csv')

len(data[data['Offensive']== 0] )


# In[3]:


len(data[data['Offensive']== 0.5] )


# In[4]:


len(data[data['Offensive']== 1.0] )


# In[5]:


data.describe()


# In[6]:


date=data.groupby(['Date'])
date_mean = data.groupby(['Date']).mean()
print(date_mean)
date_mean.to_csv("date_mean.csv", index_label="index_label")


# In[7]:


labels=['no offensive','mid offensive','offensive']
X=[148,815,72]  
colors = '#DEB887','#FFD700','#B22222'

fig = plt.figure()
plt.pie(X,labels=labels,colors=colors,autopct= '%1.1f%%') 
plt.title("The percentage of offensive degree in twitters towards Asian American before protest")


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt 

data1 = pd.read_csv('after.csv')

len(data1[data1['Offensive']== 0] )


# In[9]:


len(data1[data1['Offensive']== 0.5] )


# In[10]:


len(data1[data1['Offensive']== 1.0] )


# In[11]:


data1.describe()


# In[12]:


labels=['no offensive','mid offensive','offensive']
X=[146,715,74]  
colors = '#DEB887','#FFD700','#B22222'

fig = plt.figure()
plt.pie(X,labels=labels,colors=colors,autopct= '%1.1f%%') 
plt.title("The percentage of offensive degree in twitters towards Asian American after protest")


# In[13]:


date=data1.groupby(['Date'])
date_mean = data1.groupby(['Date']).mean()
print(date_mean)
date_mean.to_csv("date_mean1.csv", index_label="index_label")


# In[14]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df = pd.read_csv('date_mean.csv')
y = df['offensive']
x = df['date']

plt.plot(x, y)
plt.xlabel('date')
plt.xticks(rotation=75)
plt.tick_params(axis='x', labelsize=5)
plt.ylabel('offensive degree')
plt.title("The change of offensive degree in twitters towards Asian American")
plt.figure(figsize = (16, 4), dpi=300)
plt.show()


# In[94]:


import plotly
import plotly.graph_objs as go

pyplt = plotly.offline.plot
df = pd.read_csv('date_mean.csv')
x = df['date']
y = df['offensive']

trace1 = go.Scatter(
    x = x,
    y = y,
    mode = 'lines', # 线性图
    name = 'lines'
)
data = [trace1]
pyplt(data, filename='时间折线图.html')


# In[1]:


pip install wordcloud


# In[3]:


#Generate wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = "twitters1.txt"
with open(filename) as f:
    mytext = f.read()

wcloud = WordCloud(width=2800, height=1600).generate(mytext)

plt.imshow(wcloud)
plt.axis('off')
plt.show()


# In[4]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = "twitters2.txt"
with open(filename) as f:
    mytext = f.read()

wcloud = WordCloud(width=2800, height=1600).generate(mytext)

plt.imshow(wcloud)
plt.axis('off')
plt.show()


# In[ ]:




