#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install scrapy
#pip install ipython


import csv; open('proxies.csv', 'w').write('IP,Address,Port,Code,Country,Anonymity,Google,Https,Last Checked\n'); (fetch('https://free-proxy-list.net/'), [csv.writer(open('proxies.csv', 'a')).writerow(row.css('td::text').getall()) for row in response.css('table').css('tr') if len(row.css('td')) and row.css('td::text').getall()[4] == 'elite proxy' and row.css('td::text').getall()[6] == 'yes'])

