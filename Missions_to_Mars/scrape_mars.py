#!/usr/bin/env python
# coding: utf-8

# In[1]:

def scrape():
# Dependencies
    from bs4 import BeautifulSoup as bs
    import requests
    import pymongo
    from splinter import Browser
    from flask import Flask, render_template, redirect
    from flask_pymongo import PyMongo
    import pandas as pd


# In[2]:


    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # # NASA Mars News 

    # In[3]:


    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')


    # In[4]:


    # Retrieve the latest news title
    news_title=soup.find_all('div', class_='content_title')[0].text
    # Retrieve the latest news paragraph
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    print(news_title)
    print("--------------------------------------------------------------------")
    print(news_p)


    # # JPL Mars Space Images - Featured Image

    # In[5]:


    url="https://spaceimages-mars.com"
    browser.visit(url)


    # In[6]:


    # HTML object
    html=browser.html
    # Parse HTML
    soup=bs(html,"html.parser")


    # In[7]:


    img = [i.get("src") for i in soup.find_all("img", class_="headerimage fade-in")]
    img[0]


    # In[8]:


    featured_image_url=url+img[0]
    featured_image_url


    # # Mars Facts

    # In[9]:


    url="https://galaxyfacts-mars.com"
    browser.visit(url)


    # In[10]:


    tables = pd.read_html(url)
    tables


    # In[11]:


    df=tables[1]
    df.rename(columns={0: ' ',1: 'Mars'},inplace=True)
    df=df.set_index(' ')
    df


    # In[12]:


    html_table = df.to_html()
    df.to_html('table.html')
    html_table


    # # Mars Hemispheres

    # In[13]:


    url = "https://marshemispheres.com/"
    browser.visit(url)
    hemisphere_image_urls = []


    # In[14]:


    for i in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
        
        title = soup.find_all("h3")[i].get_text()
        browser.find_by_tag('h3')[i].click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        img_url = soup.find("img", class_="wide-image")["src"]
        
        hemisphere_image_urls.append({
            "title": title,
            "img_url": "https://marshemispheres.com/" + img_url
        })
        browser.back()

        title1 = hemisphere_image_urls[0]["title"]
        image1 = hemisphere_image_urls[0]["img_url"]
        
        title2 = hemisphere_image_urls[1]["title"]
        image2 = hemisphere_image_urls[1]["img_url"]

        title3 = hemisphere_image_urls[2]["title"]
        image3 = hemisphere_image_urls[2]["img_url"]

        title4 = hemisphere_image_urls[3]["title"]
        image4 = hemisphere_image_urls[3]["img_url"]
        
    hemisphere_image_urls


    # In[15]:


    browser.quit()

        # FINAL DICTIONARY FOR MONGO
        
    final_mars_data = {
    "latest_title":news_title,
    "latest_paragraph" :news_p,
    "featured_image": featured_image_url,
    "html_table": html_table,
    "hemisphere_scrape": hemisphere_image_urls,
    "title1": title1,
    "title2": title2,
    "title3": title3,
    "title4": title4,
    "image1": image1,
    "image2": image2,
    "image3": image3,
    "image4": image4,

        }

    return final_mars_data