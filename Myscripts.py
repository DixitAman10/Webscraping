#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint


# In[2]:


titles = []
By = []
Valid_till= []
Bank = []
Deal_type= []
Card_type = []


# In[3]:


headers = {"Accept-Language": "en-US, en;q=0.5"}


# In[4]:


pages = np.arange(1, 4)
pages=[1,2,3]
offers=[]
for page in pages:
    page = requests.get("https://happycredit.in/kotak-mahindra-bank-offers/?page=" + str(page), headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    offers.append(soup.find_all('a', class_='coupon-cart others'))
    sleep(randint(2,10))


# In[5]:


offers


# In[6]:


for offer in offers:
    for off in offer:
        titles.append(off.find('h3').get_text())
        By.append(off.find('p').find_all('span')[0].get_text())
        Valid_till.append(off.find('p').find_all('span')[1].get_text())
        Bank.append(off.find('p').find_all('span')[2].get_text())
        Deal_type.append(off.find('p').find_all('span')[3].get_text())
        Card_type.append(off.find('p').find_all('span')[4].get_text())


# In[7]:


offers = pd.DataFrame({
'title': titles,
'by': By,
'valid_till': Valid_till,
'bank': Bank,
'deal_type': Deal_type,
'card_type':Card_type ,
})


# In[8]:


offers.to_csv('offers.csv')


# In[9]:


df = pd.read_csv('offers.csv')


# In[10]:


df


# import schedule
# import time
# 
# def job():
#     print("I'm working...")
# 
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# 
# while 1:
#     schedule.run_pending()
#     time.sleep(1)

# In[11]:


from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print("hello world")
    #...

t = Timer(secs, hello_world)
t.start()


# In[ ]:





# The scheduler can be achieved in two ways:
#     1)Through windows
#     2)Through linux
#     Cron is used in linux & unix basically so if you can give me some more time to do it I Can resubmit it using cron job.

# In[12]:


from crontab import CronTab


# In[18]:


tab = CronTab(tabfile='Myscripts.tab')
for result in tab.run_scheduler():
    print("This was printed to stdout by the process.")


# In[ ]:




