#!/usr/bin/env python
# coding: utf-8

# ## Module 3
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
# We have loaded the data as "df" for you. Follow the instructions and finish the rest.

# In[2]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("imdb.xlsx")
from nose.tools import assert_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal


# In[3]:


# Loading the data
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

print("Data Loading Finished.")


# In[4]:


df.head()


# In[5]:


df_directors.head()


# In[6]:


df_countries.head()


# In[7]:


""" Q1: 
Join three Dataframes: df, df_directors, and df_countries with an inner join.
Store the joined DataFrames in df.

Here are the steps:
1. Merge df with df_countries and assign it df
2. Merge df with df_directors and assign it to df again
There might be errors if the merge is not in this order, so please be careful.

"""

# your code here
df = pd.merge(left = df, right = df_countries, how = 'inner', left_on = 'country_id', right_on = 'id')
df = pd.merge(left = df, right = df_directors, how = 'inner', left_on = 'director_id', right_on = 'id')
# After the join, the resulting Dataframe should have 12 columns.
df.shape


# In[8]:


assert_equal(df.shape, sol.df.shape)
print("Success!")


# In[9]:


""" Q2: 
Save the first ten rows of movie titles in a variable called first10, then print it
"""

# your code here
df_movie= df['movie_title']
first10 = df_movie[0:10]
print(type(first10))
print(first10)


# In[10]:


assert_series_equal(first10, sol.first10)
print("Success!")


# In[11]:


""" Q3: 
There's an extra character at the end of each movie title. 
Remove it from the data using str.replace.
And print the first ten rows of movie titles again. 
"""

# your code here
'''df_movie= df['movie_title'].str.replace("Ê", "")
first10 = df_movie[0:10]
print(type(first10))
print(first10)'''


# In[12]:


df["movie_title"] = df["movie_title"].apply(lambda x: x.replace("Ê", ""))
first10 = df[0:10]


# In[13]:


assert_frame_equal(df, sol.df)
print("Success!")


# In[14]:


""" Q4:
Who is the director with the most movies? First get the number of movies per "director_name", then save the director's name
and count as a series of length 1 called "director_with_most"
"""

# your code here
director_with_most = df['director_name'].value_counts()
print(director_with_most)


# In[15]:


director_with_most = df['director_name'].value_counts()[:1]
print(director_with_most)


# In[16]:


assert_series_equal(director_with_most, sol.director_with_most)
print("Success!")


# In[17]:


"""Q5:
Save all of this director's movies and their ratings in a variable called all_movies_ratings, then print this variable.
(The director with the most movies you got from the last question.)
"""

# your code here
nolan = df['director_name'] == 'Christopher Nolan'
df[nolan]


# In[18]:


#all_movie_ratings = df[nolan]['movie_title']['imdb_score'] all_movie_rating.head()
all_movies_ratings = df[nolan][['movie_title', 'imdb_score']]


# In[19]:


assert_frame_equal(all_movies_ratings, sol.all_movies_ratings)
print("Success!")


# In[56]:


"""Q6:
Recommend a **random** movie that has a rating of over 8.3. 
Store the random recommendation in a variable called "rand_goodmovie".
What is the title and imdb_score of your recommendation?
 
Here are the steps:
1. Query the data ('df' DataFrame) for movies with a rating over 8.3 (imdb_score > 8.3)
2. Create a random integer index location to get a single movie recommendation
3. Save the random movie recommendation in a DataFrame called 'rand_goodmovie'
4. Save the title of the random movie recommendation in a variable "random_title" and print it
5. Save the imdb_score of the random movie recommendation in a variable "random_imdb_score" and print it

"""
# Do not modify this part, it's needed for grading
import random
random.seed(0)

# your code here
df_imdb = df[df['imdb_score'] > 8.3]
rand_int = random.randint(0, len(df_imdb) - 1)
rand_goodmovie = df_imdb[rand_int : rand_int + 1]
random_title = rand_goodmovie['movie_title']
random_imdb_score = rand_goodmovie['imdb_score']


# In[42]:


df.head()


# In[43]:


#imdb83 = df['imdb_score'] > 8.3
#df_imdb = df['imdb83']
#df_imdb

df_imdb = df[df['imdb_score'] > 8.3]
df_imdb.head()


# In[44]:


df_imdb.shape


# In[51]:


rand_int = random.randint(0, len(df_imdb) - 1)


# In[52]:


rand_goodmovie = df_imdb[rand_int : rand_int + 1]
rand_goodmovie


# In[54]:


random_title = rand_goodmovie['movie_title']
random_title


# In[55]:


random_imdb_score = rand_goodmovie['imdb_score']
random_imdb_score


# In[57]:


from nose.tools import assert_in
assert_in(rand_goodmovie[["movie_title", "imdb_score"]].values, sol.possible_goodmovies[["movie_title", "imdb_score"]].values)
assert_equal(random_title.iloc[0], rand_goodmovie["movie_title"].iloc[0])
assert_equal(random_imdb_score.iloc[0], rand_goodmovie["imdb_score"].iloc[0])
print("Success!")


# In[ ]:




