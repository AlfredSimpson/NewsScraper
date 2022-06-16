from bs4 import BeautifulSoup
import requests, time

"""
This was built following basic instructions from Pythonology's  YouTube Video,
'Python RSS Feed reader with BeautifulSoup'. It also utilizes the lxml modules. After watching the video and completing the basic set up, I implemented mulutiple sources and made significant changes to the basic program that was constructed. Ultimately this intended to be used by a discord bot, which will post it on the server it is installed in. 

This program repeats every 30 minutes. If no changes to the news exist, it will not post links but currently will post a message letting you know that the source without changes had nothing to report. 

Language: Python 3.10
Date: June 15, 2022
Author: Alfred Simpson

TODO: Extra features I may implement include:
- Adding sources
- Automating the dictionary (either slicing from xml or getting user input)
- Giving the user the option to set the frequency of checking
- Allowing multiple articles
- Checking for similar articles.
"""

mostRecent = []
noNews = []

sources = ['https://www.wired.com/feed/category/security/latest/rss', 'https://threatpost.com/feed/',
           'http://feeds.feedburner.com/TheHackersNews?format=xml', 'https://krebsonsecurity.com/feed/', 'https://www.darkreading.com/rss.xml']

numSources = len(sources)

for i in range(numSources):
    mostRecent.append(i)

sourceDict = {
    0   :   "Wired", 
    1   :   "ThreatPost",
    2   :   "The Hackers' News",
    3   :   "Krebs on Security",
    4   :   "Dark Reading"
    }


def checkPosted(output, sourceNum, article):
    if output in mostRecent:
        noNews.append(sourceDict[sourceNum])
        return
    else:
        # output = summary(article)
        mostRecent[sourceNum] = output
        print(output)

"""
*** Summary is not currently used. It's purpose is for allowing quick snippets of articles and for checking multiple articles from a source ***
def summary(article):
    title = article.title.text
    snippet = article.description.text
    link = article.link.text
    output = (f"Title: {title}\n\nSnippet: {snippet}\n\nLink: {link}\n\n--------\n\n")
    return output

"""
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

        checkPosted(output, count, articles[0])
        count += 1
    if len(noNews) > 0:
        print("\nThe following source(s) had nothing new to report: \n")
        print(*noNews, sep=", ", end="\n\n")

#setTimer is currently not being used. It's intent is to simply take the input from a user and translate it into seconds. Anticipated issue: user might not enter digits, might ctrlC, etc. Need to implement a try/except/catch/finally
def setTimer():
    minutes = input("How many minutes should I wait between checking the news? ")
    timer = minutes * 60

while(True):
    checkTheNews()
    print("\n\nGiving time for you to read\n\n")
    noNews.clear()
    time.sleep(5)
    # time.sleep(1800)


