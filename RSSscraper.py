from bs4 import BeautifulSoup
import requests

"""
This was built following basic instructions from Pythonology's  YouTube Video,
'Python RSS Feed reader with BeautifulSoup'. It also utilizes the lxml modules. After watching the video and completing the basic set up, I intend to source multiple sites and feed this to the discord bot, which will post it on the server it is installed in. 
"""
# TODO: Delete after all sources compiled - Wired,ThreatPost, The Hackers news use the same layout: title, description, pubDate (not currently used, but shows when published), and link without href attributes. As these sources seem uniform, we can use one block of code to iterate through them.

mostRecent = []

sources = ['https://www.wired.com/feed/category/security/latest/rss', 'https://threatpost.com/feed/',
           'http://feeds.feedburner.com/TheHackersNews?format=xml', 'https://krebsonsecurity.com/feed/', 'https://www.darkreading.com/rss.xml']

numSources = len(sources)

for i in range(numSources):
    mostRecent.append(i)

def checkPosted(link, sourceNum, article):
    if link in mostRecent:
        return
    else:
        output = summary(article)
        mostRecent[sourceNum] = output
        print(output)

def summary(article):
    title = article.title.text
    snippet = article.description.text
    link = article.link.text
    output = (f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")
    return output

count = 0
def checkTheNews():
    count = 0
    for source in sources:
        url = requests.get(source)
        soup = BeautifulSoup(url.content, 'xml')
        articles = soup.find_all('item')
        
        title = articles[0].title.text
        snippet = articles[0].description.text
        link = articles[0].link.text
        output = (f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")

        checkPosted(link, count, articles[0])
        count += 1
checkTheNews()
# print(*mostRecent, sep= "\n\n")

