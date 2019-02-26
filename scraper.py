# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
# print this
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("li p a")
#
matchedlinks=root.cssselect("li p a")
# print(matchedlinks)
record={}
counter=100
for li in matchedlinks[100:200]:
  counter=counter+1
  print(counter)
  listtext=li.text_content()
  print(listtext.encode('utf-8'))
  record['address'] = listtext
  scraperwiki.sqlite.save(['address'],record)
  record['link'] = li.attrib['href']
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
