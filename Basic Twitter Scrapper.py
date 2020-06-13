#Function Declaration
# Function Steps in Line
# 1. Get URL of the webpage that needs scraping. Get the reference HTML tags that will assist in string exrtaction
# 2. Initialize the browser instance using webdriver
# 3. Logic: 
# Loop (Iterate it the number of times the HTML's starting tag appears in the code)
       # Extract the string between HTML's starting and ending tags
       # increase the TAG's index counts by 1 every time to avoid extracting same string and move forward with other instances of the tag.
# Store the results in a list
# Use the list as twitter status

# What is a Twitter Status?
# IT will be a string found between  "</span></div><a href=\"/","\" dir=\"auto\"" and   "\" dir=\"auto\"" of inspect element's page source of a twitter page. These will be the start and end tags for us mentioned above.    

# 4. Use the twitter status list elements obtained above and concatenate each element with "https://twitter.com/" to form a new URL to search.
        # Actually first webpage will not be having any actual texts of a tweet. IT will basically be an API kinda thing that upon cilcking will get Twitter Status as value
        # to further load the actual tweet's page where in between the TITLE tags the actual tweet text will lie..
        # We are supposed to extract that from this code
        
# 5. Use the above status made URLs to re-search twitter and get all that is written between the TITLE tags of page source HTML.
# 6. Store above results in list and output the list.  Waouh ! ou !! we have a list of tweets   
###################################################################################################################



#Library Import

from selenium import webdriver
    
def get_twitter_status(URLS,start_string,end_string):
    driver = webdriver.Chrome('C:/Users/MEHUL/chromedriver')
    driver.get(URLS)
    html = driver.page_source
    start_string_cnt = html.count(start_string)
    start_string_index = html.find(start_string)
    start_string_length = len(start_string)
    end_string_index = html.find(end_string,start_string_index)
    start_string_index += 1
    end_string_index += 1
    tweets = list()
    for x in range(start_string_cnt-1):
        start_string_index =  html.find(start_string,start_string_index)
        end_string_index = html.find(end_string,start_string_index)
        tweets.append(html[start_string_index+start_string_length:end_string_index])
        start_string_index += 1
        end_string_index += 1   
    for x in tweets:
        if x.count("signup") > 0:
            tweets.remove(x)
    return(tweets)

def get_actual_tweets(URLS,start_string,end_string):
    driver = webdriver.Chrome('C:/Users/MEHUL/chromedriver')
    driver.get(URLS)
    html = driver.page_source
    start_string_cnt = html.count(start_string)
    start_string_index = html.find(start_string)
    start_string_length = len(start_string)
    end_string_index = html.find(end_string,start_string_index)
    tweet = html[start_string_index+start_string_length:end_string_index]
    print(tweet)
    return(tweet)
    
twitter_handle_id = 'MY TWITTER ID without @' #Getting the Twitter HAndle
twitter_urls = "https://twitter.com/"+twitter_handle_id #Comverting the Twitter HAndle in to a URL
tweet_lists = get_twitter_status(twitter_urls,"</span></div><a href=\"/","\" dir=\"auto\"")#Fetching the Tweets that come under FIRST 'zero length SCROLL' window upon load

tweet_urls = list()
for x in range(len(tweet_lists)-1):
    tweet_urls.append("https://twitter.com/"+tweet_lists[x])#Converting every single tweets in to a URL

final_tweet_list = list()
for x in tweet_urls:
    final_tweet_list.append(get_actual_tweets(x,"<title>","</title>"))#Extracting the actual tweets
    
print(final_tweet_list)    #outputting the final tweets. Same can be done in a Data Frame and be stored in an excel.



###################################################################################################################
#PLEASE NOTE: Above functions can be used multiple times to get tweets out of tweet pages where in other users have commented something under a main tweet.
#Also to get all the tweets of an account we'' need to use FULL LENGTH SCROLL FUNCTIONALITY of selenium.
#Learning
# 1. Webpage is basically a forest of HTML TAGs.
# 2. We only need to find the TREE of which the fruit we intend to taste.
# 3. This code explains how it can be done manually.
# 4. Same can be done in creame and sophisticated manner using already available SCRAPPER tools online.
