#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install scrapy
# pip install ipython

import csv; [[fetch('https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false&index=' + str(page * 24)), [csv.DictWriter(open('rightmove.csv', 'a'), ['title', 'url', 'address', 'price', 'description', 'date']).writerow({'title': card.css('h2[class="propertyCard-title"]::text').get().strip(), 'url': card.css('a[class="propertyCard-link"]::attr(href)').get(), 'address': card.css('address[class="propertyCard-address"] *::text').getall()[-2], 'price': card.css('div[class="propertyCard-priceValue"]::text').get().strip(), 'description': card.css('span[itemprop="description"] *::text').get(), 'date': ' '.join(list(filter(None, [text.strip() for text in card.css('div[class="propertyCard-branchSummary"] *::text').getall()])))}) for card in response.css('div[class="propertyCard-wrapper"]')]][-1] for page in range(0, 4)]

