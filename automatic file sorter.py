#!/usr/bin/env python
# coding: utf-8

# In[2]:


## high level operation of out file in the file explorer
import os, shutil


# In[14]:


## changing from back slash to foward slash and adding one at the end
path = r'C:/Users/Administrator/Pictures/Camera Roll/'


# In[18]:


##checking the type ofitems we have in that folder
file_name = os.listdir(path)


# In[17]:


## cheking if a path exists or not and create if it does not exist
folder_name = ['csv files', 'image files', 'txt files']
for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
        os.makedirs((path + folder_name[loop]))


# In[27]:


## checking the files and putting it to the right folder
for file in file_name:
    file_path = path + file
    if os.path.isfile(file_path):
        if file.endswith('.csv'):
            dest_path = path + "csv files/" + file
            shutil.move(file_path, dest_path)
        elif file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  
            dest_path = path + "image files/" + file
            shutil.move(file_path, dest_path)
        elif file.endswith('.txt'):
            dest_path = path + "text files/" + file
            shutil.move(file_path, dest_path)
        else:
            print(f"File '{file}' doesn't match any category")
    else:
        print(f"'{file_path}' is not a file or doesn't exist")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




