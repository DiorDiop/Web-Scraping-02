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
job_poster = []
job_pricing = []
job_location = []


# In[3]:


# Get the title
html = urlopen("https://www.guru.com/d/freelancers/skill/Data-science/")
bso = soup(html.read())
for link in bso.find_all('h2', {'class' : 'serviceListing__title serviceListing__title--dark'}):
    print(link.a.text)


# In[17]:


# Get Job pricing
for job in bso.find_all('p', {'class' : 'serviceListing__rates'}):
    print(job.text.strip())


# In[5]:


#  Get Freelancer name
for job in bso.find_all('h3', {'class' : 'freelancerAvatar__screenName'}):
    print(job.a.text)


# In[18]:


# Get freelancer location and revenue per year
for job in bso.find_all('p', {'class' : 'freelancerAvatar__meta'}):
    print(job.span.text)
    if span is not None:
        print(span.text.strip())
    else:
        print(" ")


# In[7]:


# Get freelancer description
for job in bso.find_all('p', {'class' : 'serviceListing__desc'}):
    print(job.text)


# In[8]:


# Get freelancer skills
for job in bso.find_all('div', {'class' : 'skillsList'}):
    print(job.a.text)


# In[9]:


for job in bso.find_all('a', {'class' : 'skillsList__skill skillsList__skill--hasHover'}):
    print(job.text)


# In[10]:


def freelance(webpage):
    crawl = urlopen(webpage)
    bsobj = soup(crawl.read())
    bsobj_title = bsobj.find_all('h2', {'class' : 'serviceListing__title serviceListing__title--dark'})
    bsobj_pricing = bsobj.find_all('p', {'class' : 'serviceListing__rates'})
    bsobj_name = bsobj.find_all('h3', {'class' : 'freelancerAvatar__screenName'})
    bsobj_location = bsobj.find_all('p', {'class' : 'freelancerAvatar__meta'})
    for x in range(len(bsobj_title)):
        job_titlt.append(bsobj_title[x].a.text)
        job_pricing.append(bsobj_pricing[x].text)
        job_poster.append(bsobj_name[x].a.text)
        job_location.append(bsobj_location[x].span.text)

        
webpage = 'https://www.guru.com/d/freelancers/skill/Data-science/'
page = 0
for i in range(1, 1752):
    page = page + 1
    webpage = webpage + str(page)
    freelance(webpage)


# In[16]:


for job in bso.find_all('p', {'class': 'freelancerAvatar__meta'}):
    span = job.find('span')  # Look for the <span> tag within the <p> element
    if span is not None:
        print(span.text.strip())
    else:
        print(" ")


# In[ ]:





# In[ ]:




