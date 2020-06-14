#For it to Work please input correct Names with no spelling mistakes. It is a basic code with no aritifial intelligence

# #############WIKIPEDIA SCRAPPER#####################
# Objective: Builda scrapper that searches our desired term on google and returns with an intorductory paragraph of on that term 
           # from wikipedia according to the page sorted out by google bsis the popularity of the subject
# Functionality similar to: Google assistant. When we ask questions like "DO YOU KNOW SHAHRUKH KHAN", It replies back with a little gist "AS PER WIKIPEDIA"

# I have tried to recreate a similar sort of functinaliy with not more than 0.01% semblance...LMAO

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib


def get_wikipedia_url(Search_Term):
    allowed_url="http" #we only want HTTP type of URLs
    not_allowed_url="googleusercontent"                                             #We don't want stray account related URLs popping up
    Google_Url = "https://www.google.com/search?q={}".format(urllib.parse.quote(Search_Term)) #Here we combine the search term with regular Google search URL template to get final URL
    driver = webdriver.Chrome('C:/Users/MEHUL/chromedriver 83')                     #Loading the chrome driver instance
    driver.get(Google_Url)                                                          #Establishing connection with the URL
    html_text = driver.page_source                                                  #Reading the page source HTML
    soup_object = BeautifulSoup(html_text, 'html.parser')                           #Loading the Soup parser
    my_tags = soup_object.find_all('a')                                             #Seperating all the anchor tags [It is between anchor tags that our tons of URLs reside]
    URL = list() 
    for link in my_tags:
        URL.append(link.get('href'))                                                #From the RESULT_SET object of SOUP get all the HREF links      
    URL1 = list(filter(None, URL))                                                  #Filter all the null values from list as NULL is not iterable
    URL2 = list(filter(lambda x: allowed_url in x, URL1))                           #Filter only HTTP type URLs. IT will be huge list with youtube videos and what not
                                                                                    #Above list can also be used to scrape other URLs besides wikipedia.
    URL3 = list(filter(lambda x: not_allowed_url not in x, URL2))                   #Filter all the account related URLs
    final_url_list = list(filter(lambda x: "wikipedia" in x and urllib.parse.quote(Search_Term).replace("%20","_").lower() in x.lower(), URL3))
    wikipedia_url = ''
    if len(final_url_list) > 1:
        wikipedia_url = min(final_url_list,key = len)
    else:
        wikipedia_url = final_url_list[0]
                #Get only those URLs that have our search term as well as "wikipedia" in it. Also get the shortest of those URLs.WHY??
                #Becasue we need the introduction part only. Other URLs will have extras embedded alongside the main search term that google will have displayed.
                #We dont want them. in that case the smallest length URL will be the one with only search term. Anything extra will have a longer URL.
    return(wikipedia_url)

def get_topic_introduction(wikipedia_scrape):
    driver = webdriver.Chrome('C:/Users/MEHUL/chromedriver 83')
    driver.get(wikipedia_scrape)
    html_text = driver.page_source
    soup_object = BeautifulSoup(html_text, 'html.parser')
    for x in soup_object.find_all('p'):
        print(x.getText()) #Get elements of Paragraph tag
    #print(my_tags)
    

get_topic_introduction(get_wikipedia_url("Sushant Singh Rajput"))    

#Few Terms I Tried and which gave me succesful outputs:
# 1. Assassin's Creed Valhalla
# 2. Shahrukh Khan
# 3. Amitabh Bachchan
# 4. Matrix
# 5. Corona
# 6. Bill Gates
# 7. Atal bihari vajpayee
# 8. Naredra Modi
