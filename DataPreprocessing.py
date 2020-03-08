#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing

# In[1]:


import pandas as pd


# ##### Data from Krish's repository.

# In[2]:


data = pd.read_csv('./Data/tsvFiles/data_krish.tsv', sep = '\t')

print(data.shape)

data.head()


# In[21]:


data['Strength'].value_counts()


# In[22]:


data.drop_duplicates(subset = 'Password', keep = 'first', inplace = True)


# In[23]:


data0 = data[data['Strength'] == 0]
data1 = data[data['Strength'] == 1]
data2 = data[data['Strength'] == 2]


# In[24]:


data2.head()


# In[25]:


print("data0 shape : ", data0.shape)
print("data1 shape : ", data1.shape)
print("data2 shape : ", data2.shape)


# In[28]:


data.dtypes


# In[36]:


data1 = data1.sample(frac = 0.45)


# ##### Data from Common.tsv

# In[37]:


commonData = pd.read_csv('./Data/tsvFiles/common.tsv', sep = '\t')

print('Common data shape: ', commonData.shape)

commonData.head()


# In[38]:


common = pd.concat([commonData, data0], axis = 0)

common.head()


# In[39]:


common = common.drop_duplicates(subset = 'Password', keep = 'first')

print("Passwords having strength = 0 : ", common.shape[0])

common.head(3)


# ##### Data from strong.tsv

# In[40]:


strongData = pd.read_csv('./Data/tsvFiles/strong.tsv', sep = '\t')

# shuffle
strongData = strongData.sample(frac = 1)
strongData = strongData.sample(frac = 1)
strongData = strongData.sample(frac = 1)
strongData = strongData.sample(frac = 1)

print('Strong data shape: ', strongData.shape)

strongData.head()


# In[41]:


strong = pd.concat([strongData, data2], axis = 0)


# In[42]:


strong.drop_duplicates(subset = 'Password', keep = 'first', inplace = True)

print('Passwords having strength = 0 : ', strong.shape[0])


# ###### Combine common, data1, strong

# In[43]:


df = pd.concat([common, data1, strong], axis = 0)

#shuffle
df = df.sample(frac = 1)
df = df.sample(frac = 1)
df = df.sample(frac = 1)

df.drop_duplicates(subset = ['Password'], keep = 'first', inplace = True)


df['Strength'].value_counts()


# In[44]:


df.head()


# In[45]:


df.tail()


# ##### Save df

# In[48]:


df.to_csv('./Data/tsvFiles/data.tsv', sep = '\t', index = False)


# #### Creating tf-idf vector for each password

# In[49]:


def word_divide_char(X):
    return list(X)


# In[52]:


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(tokenizer = word_divide_char, encoding='utf-8')

X = vectorizer.fit_transform(data['Password'].values.astype('U'))


# In[61]:


X[:3, :].toarray()

