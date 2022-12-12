#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# [Работа с названиями колонок](#Columns)
# 

# [Работа с пропусками](#Nan)

# [Работа с дубликатами](#dupli)

# In[2]:


df = pd.read_csv('yandex_music_project.csv')


# In[3]:


df.info()


# ### Работа с названиями колонок
# <a id='Columns'></a>

# In[12]:


#Убираю пробелы,заглавные буквы,привожу к общему стилю наименование столбцов в дата-фрейме
df.rename(columns={"userID":"user_id","City":"city","Day":"day","Track":"track"}, inplace=True)
df.columns = df.columns.str.replace(' ', '')


# In[13]:


df.info()


# ### Работа с пропусками
# <a id='Nan'></a>

# In[29]:


# подсчёт пропусков
df.isna().sum()


# In[17]:


# перебор названий столбцов в цикле и замена пропущенных значений на 'unknown'
columns_to_replace = ['track','artist','genre']
for column in columns_to_replace:
    df[column] = df[column].fillna('unknown')


# In[30]:


# подсчёт пропусков
df.isna().sum()


# ### Работа с дубликатами
# <a id='dupli'></a>

# In[25]:


# подсчёт явных дубликатов
df.duplicated().sum()


# In[26]:


# удаление явных дубликатов
df = df.drop_duplicates()


# In[27]:


# проверка на отсутствие дубликатов
df.duplicated().sum()


# In[35]:


df['genre'].sort_values().unique()


# In[36]:


df['genre'] = df['genre'].replace(['hip','hop','hip-hop'],'hiphop')


# In[37]:


df['genre'].sort_values().unique()


# In[42]:


df.groupby('city')['time'].count()


# In[43]:


df.groupby('day')['time'].count()


# In[54]:


def number_tracks(day,city):
    track_list = df[(df['day']==day)&(df['city']==city)]
    track_kist_count = track_list['user_id'].count()   
    return track_kist_count


# In[55]:


number_tracks('Monday','Saint-Petersburg')


# In[56]:


number_tracks('Wednesday', 'Moscow')


# In[58]:


data = [
    ['Moscow', 15740, 11056, 15945],
    ['Saint-Petersburg', 5614, 7003, 5895]]
columns = ['city', 'monday', 'wednesday', 'friday']


# In[59]:


pd.DataFrame(data=data,columns=columns)


# In[60]:


moscow_general = df[df['city']=='Moscow']


# In[61]:


spb_general = df[df['city']=='Saint-Peterburg']


# In[62]:


def genree_weekday(table, day, time1, time2):
    df = table
    genre_df = df[df['day']==day]
    genre_df = genre_df[genre_df['time']<time2]
    genre_df = genre_df[genre_df['time']>time1]
    genre_df_grouped = genre_df.groupby('genre')['genre'].count()
    genre_df_sorted = 


# In[ ]:




