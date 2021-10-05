#!/usr/bin/env python
# coding: utf-8

# ## Module 4
# 
# #### In this assignment, you will continue working on the movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names
# 
# We have loaded and joined the data as "df" for you. Follow the instructions and finish the rest part.

# In[9]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("imdb.xlsx")
from nose.tools import assert_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal


# In[10]:


# Loading the data
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

df = pd.merge(left=df, right=df_countries, 
              how='inner', left_on='country_id', 
              right_on='id')

df = pd.merge(left=df, right=df_directors, 
              how='inner', left_on='director_id', 
              right_on='id')

print("Finished.")


# In[11]:


df.head(5)


# In[40]:


""" Q1: 


"""

# your code here
#pd_drop = df.drop(['director_id', 'country_id', 'content_rating', 'title_year', 'duration', 'id_x', 'country', 'id_y', 'director_name'], axis = 1)

use = ['imdb_score', 'gross']

#df[use].head
#score_gross_description = df_use.pivot_table(
    #df, index = ['movie_title'], columns = ["imdb_score"])
score_gross_description = df[use].describe()
print(score_gross_description)


# In[41]:


assert_frame_equal(score_gross_description, sol.score_gross_description)
print("Success!")


# In[ ]:


"""Q2:
What is the average rating of the director Christopher Nolan's movies? Save this value in a variable called nolan_mean and 
print.
"""

# your code here


# In[43]:


Nolan = df['director_name'] == 'Christopher Nolan'
df[Nolan]


# In[44]:


nolan_mean = df[Nolan]['imdb_score'].mean()
print(nolan_mean)


# In[45]:


assert_equal(nolan_mean, sol.nolan_mean)


# In[48]:


"""Q3: 
Create a series called 'directors' that contains each director's name and his or her average rating.  Print out the type of your variable.
Use the 'directors' series to find the average rating for Steven Spielberg.  Print the value.
"""

# your code here


directors = df.groupby(['director_name']).mean()['imdb_score']

print(type(directors))


# In[53]:



directors['Steven Spielberg']


# In[54]:


assert_series_equal(directors, sol.directors)
print("Success!")


# In[58]:


"""Q4:
Select the non-USA movies made after 1960 by Hayao Miyazaki.
Save the result in a DataFrame called 'miyazaki', then print it.

Here are the steps:
1. Query the data ('df' DataFrame) based on the following conditions:
- Non-USA movies (country_id != 1)
- Movies made after 1960 (title_year > 1960)
- Movies made by director Hayao Miyazaki (director_id == 46)
2. Save the filtered data in a DataFrame called 'miyazaki' and print it

"""

# your code here
exUSA = df['country'] != 'USA'
after1960 = df['title_year'] > 1960
#df_1960 = df[after1960]
director = df['director_id'] == 46

miyazaki = df[exUSA & after1960 & director]

print(miyazaki)


# In[59]:


assert_frame_equal(miyazaki, sol.miyazaki)
print("Success!")


# In[104]:


"""Q5: 
Create a Pivot Table that shows the median rating for each director, grouped by their respective countries. Name your variable
'pivot_agg'
"""

# your code here
import numpy as np
pivot_agg = pd.pivot_table(
    df, index = ['country', 'director_name'],
    values = ['imdb_score'],
    aggfunc = [np.median])
    
pivot_agg


# In[105]:


assert_frame_equal(pivot_agg, sol.pivot_agg)
print("Success!")


# In[106]:


"""Q6:
How long did the movie Gladiator aim to keep your attention? Save the series with this information
in a variable called 'gladiator_duration', then print it.
"""

# your code here
gladiator = df['movie_title'] == 'Gladiator'
gladiator_duration = df[gladiator]['duration']


# In[107]:


assert_series_equal(gladiator_duration, sol.gladiator_duration)
print("Success!")


# In[ ]:




