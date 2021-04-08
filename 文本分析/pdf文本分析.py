#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pdfplumber
import pandas as pd


# # 直接提取文本

# In[6]:


with pdfplumber.open('C:/Users/Bearlining/Desktop/600816.pdf') as pdf:
    content = ''
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        page_content = '\n'.join(page.extract_text().split('\n')[:-1])
        content = content + page_content
with open("年报.txt", mode="w", encoding="utf-8") as f:
    f.write(content)


# # 提取表格

# In[8]:


with pdfplumber.open('C:/Users/Bearlining/Desktop/600816.pdf') as pdf:
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        for table in page.extract_tables():
            df1 = pd.DataFrame(table)
            df = df.append(df1)
df.to_excel('年报.xlsx')


# In[5]:





# In[10]:





# In[ ]:




