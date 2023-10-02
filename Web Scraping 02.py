#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests
import re
import pandas as pd


# In[2]:


# Create empty lists to stores data later
job_title = []
job_name = []
job_poster = []
job_pricing = []
job_location = []


# In[4]:


# get url
html = urlopen("https://www.guru.com/d/freelancers/skill/Data-science/")
bso = soup(html.read())
for link in bso.find_all('h2'):
    print(link.a)


# In[4]:


# get the html code
soup = soup(page.text, 'html')
soup


# In[5]:


title = soup.find_all('h2')
title


# In[ ]:





# In[ ]:





# In[ ]:




