
# coding: utf-8

# In[32]:

import pandas as pd
import requests


# In[33]:

# get a df of URLs along with corresponding titles
df = pd.read_csv("https://eesposito.com/pds/pds_videos.csv")


# In[ ]:

# loop through each row
for i,title,urlstr in df.itertuples():
    
    # create output filename
    filename = title.replace(":","").replace("/","") + ".mp4"
    
    print "fetching ",urlstr
    print "outputing to ", filename 
    
    
    with open(filename, 'wb') as output_file:
        # fetch the url
        response = requests.get(urlstr, stream=True)
        if not response.ok:
            print "error"
        for block in response.iter_content(1024):
            output_file.write(block)


# In[ ]:



