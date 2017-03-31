import sys
import feedparser

for RSS_URL in sys.argv[1:]:

    feed = feedparser.parse(RSS_URL)
    feed_length = len(feed.entries)
    feed_statement = "Feed length: "
    feed_length_statement =  feed_statement + str(feed_length)

    if feed.bozo == 0:
        print("Awesomesauce. This is a well-formed feed!\n")
    else:
        print("Ruh roh. Potential trouble ahead.\n")

    print("Feed title: " + feed.feed.title)
    print("Feed link: " + feed.feed.link)
    print("Feed description: " + feed.feed.description)
    print("Feed published date: " + feed.feed.published)
    print(feed_length_statement)
    print("\n")

    i = 0
    for entry in feed.entries:
        print(i, feed.entries[i].title)
        i += 1
    else:
        print("Hoorah! You've reached the end of the entry titles.\n")

    i = 0
    for entry in feed.entries:
        print(i, feed.entries[i].description)
        i += 1
    else:
        print("The end is here. This is the last entry description.\n")
