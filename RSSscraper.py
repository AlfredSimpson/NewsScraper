from bs4 import BeautifulSoup
import requests

"""
This was built following basic instructions from Pythonology's  YouTube Video,
'Python RSS Feed reader with BeautifulSoup'. It also utilizes the lxml modules. After watching the video and completing the basic set up, I intend to source multiple sites and feed this to the discord bot, which will post it on the server it is installed in.
"""

url = requests.get('https://www.wired.com/feed/category/security/latest/rss')

#Note, printing url should say Response[200] if accessible
#print(url)

soup = BeautifulSoup(url.content, 'xml')

items = soup.find_all('item') 

for item in items:
    title = item.title.text
    snippet = item.description.text
    link = item.link
    print(f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")

"""
Note: the above iterates over all items within the feed. the specific information it is searching for is dependent upon the individual site and how they have laid things out. The video uses summary, as the feed they are working off of uses summary tags. Further, wired simply links, but does not use href attributes. If they did, they link portion should look like this:
link = item.link['href']
"""

#TODO: compile all sources, keep track of last title. Create an if statement that references the LAST article posted by publishing date or simply is put in a temporary list for each site and says 'if x in y don't post, else, post, replace x in y with the new article'.