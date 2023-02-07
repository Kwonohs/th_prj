import feedparser
myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")
print("피드 제목 :", myFeed['feed']['title'])
print("포스트 수 :", len(myFeed.entries))
post = myFeed.entries[0]
print("포스트 제목: ", post.title)

content = post.content[0].value #이것도 content error 가있는데 어찌해야할까
print("콘텐츠 원본 :\n", content)

