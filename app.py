#save docs search rank
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import requests
import pandas as pd
# is there a better one than looker.com/robots.txt or https://fr.looker.com/sitemap_en.xml site map?

#all_docs = pd.read_csv('~/DOCS.csv')
#print(all_docs)

def scrapper_function(doc):
    doc = str(doc)
    req = Request(doc)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    strings = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
        strings.append(link.string)
    done_links = []
    done_text = []
    val = 0
    for val in range(len(links)):
        try:
            if str(links[val]).startswith("/") or str(links[val]).startswith("#"):
                newlink = "https://docs.looker.com" + str(links[val])
                #print(newlink)
                done_links.append(newlink)
                #print(newlink)
                #print(strings[val])
                done_text.append(strings[val])
            
            elif str(links[val]).startswith("d"):
                newlink = "https://docs.looker.com/" + str(links[val])
                done_links.append(newlink)
                #print(newlink)
                done_text.append(strings[val])

            else:
                #print(href)
                done_links.append(str(links[val]))
                #print(str(links[val]))
                done_text.append(strings[val])
        except ValueError:
            pass
        val = val + 1
    #print(done_links)
    bad_actors = []
    bad_strings = []
    print("ready")
    count = 0
    new_val = 0
    for new_val in range(len(done_links)):
        response = requests.get(done_links[new_val])
        count = count + 1
        print(count)
        print(response.status_code)
        print(done_links[new_val])
        print(done_text[new_val])
        if response.status_code != 200:
            #print(response.status_code)
            #print(final)
            bad_actors.append(done_links[new_val])
            bad_strings.append(done_text[new_val])

        print("done")
        #print(bad_actors)
        #print(bad_strings)
    #df = pd(bad_actors, columns=['https://docs.looker.com/dashboards'])
    # file = open('bad_actors.csv','w')
    # file.write(bad_actos)
    # file.close()

scrapper_function("https://docs.looker.com/exploring-data/retrieve-chart-intro")
