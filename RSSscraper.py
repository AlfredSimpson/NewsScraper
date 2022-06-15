from bs4 import BeautifulSoup
import requests

"""
This was built following basic instructions from Pythonology's  YouTube Video,
'Python RSS Feed reader with BeautifulSoup'. It also utilizes the lxml modules. After watching the video and completing the basic set up, I intend to source multiple sites and feed this to the discord bot, which will post it on the server it is installed in. 
"""
mostRecent = ['0', '2', '3',]
url = requests.get('https://www.wired.com/feed/category/security/latest/rss')

# Note, printing url should say Response[200] if accessible
# print(url)

soup = BeautifulSoup(url.content, 'xml')

items = soup.find_all('item')

for item in items:
    title = item.title.text
    snippet = item.description.text
    link = item.link.text
    output = (
        f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")
    mostRecent.append(output)
    print(
        f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")
    print(mostRecent[0])

"""
The above iterates over all items within the feed. the specific information it is searching for is dependent upon the individual site and how they have laid things out. The video uses summary, as the feed they are working off of uses summary tags. Further, wired simply links, but does not use href attributes. If they did, they link portion should look like this:
        link = item.link['href']

Further, my code deviates from the video linked here. 

I've created an array, mostRecent. mostRecent will be an array consisting of the most recent articles from each source. As Wired is the first source, they will always be mostRecent [0]. This is for a future project which will incorporate this scraper and push the relevant information to a Discord Bot.
"""

# TODO: compile all sources, keep track of last title. Create an if statement that references the LAST article posted by publishing date or simply is put in a temporary list for each site and says 'if x in y don't post, else, post, replace x in y with the new article'.

# TODO: Delete after all sources compiled - Wired,ThreatPost, The Hackers news use the same layout: title, description, pubDate (not currently used, but shows when published), and link without href attributes. As these sources seem uniform, we can use one block of code to iterate through them.

sources = ['https://www.wired.com/feed/category/security/latest/rss', 'https://threatpost.com/feed/',
           'http://feeds.feedburner.com/TheHackersNews?format=xml', 'https://krebsonsecurity.com/feed/', 'https://www.darkreading.com/rss.xml']


for source in sources:
    count = 0
    url = requests.get(source)
    soup = BeautifulSoup(url.content, 'xml')
    articles = soup.find_all('item')

    for article in articles[:3]:
        title = article.title.text
        snippet = article.description.text
        link = article.link.text
        output = (
            f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")
        print(output)
    for item in items[:1]:
        if item[0].link.text not in mostRecent:
            if count == 0:
                mostRecent[0] = output
            elif count == 1:
                mostRecent[1] = output
            elif count == 2:
                mostRecent[2] = output
            else:
                continue

"""
Pseudocode:
For every site listed in sources, isolate the url
Then, feed the url to BeautifulSoup
Then go through the xml document and find all "items", which is how most sites post their articles.
Then for the first 3 articles, do the following:
Get the title, snippet/description, and link. 
Print the output (this will be removed for the bot).

We also want this:
For the first article only: 
if this article is in our parent list, mostRecent,
"""

# This currently iterates over the top 3 news stories of these vetted sources: Wired, ThreatPost, TheHackersNews, Krebs on Security, Dark Reading
