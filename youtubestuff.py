import umarutils as u

import gdata.youtube
import gdata.youtube.service

# yt_service = gdata.youtube.service.YouTubeService()
# yt_service.ssl = True

def getfeed(uri):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    feed = yt_service.GetYouTubeVideoFeed(uri)
    entries = []
    for entry in feed.entry:
        entries.append(entrydetails(entry))
    return entries

def entrydetails(entry):
    e = []
    if entry.id.text:
        e.append(["id",entry.id.text.split("/")[-1]])
    if entry.media.title:
        e.append(['Video title',entry.media.title.text])
    if entry.published:
        e.append(['Video published on',entry.published.text])
    if entry.media.description:
        e.append(['Video description',entry.media.description.text])
    if entry.media.category:
        e.append(['Video category',entry.media.category[0].text])
    if entry.media.keywords:
        e.append(['Video tags',entry.media.keywords.text])
    if entry.media.player:
        e.append(['Video watch page',entry.media.player.url])
    if entry.GetSwfUrl():
        e.append(['Video flash player URL',entry.GetSwfUrl()])
    if entry.media.duration:
        e.append(['Video duration',entry.media.duration.seconds])
    
    # non entry.media attributes
    if entry.geo:
        e.append(['Video geo location',
                  [str(entry.geo.location()[0]),
                   str(entry.geo.location()[1])]])

    if entry.statistics:
        e.append(['Video view count',entry.statistics.view_count])

    if entry.rating:
        e.append(['Video rating',entry.rating.average])
        
    # show alternate formats
    if entry.media.content:
        for alternate_format in entry.media.content:
            if 'isDefault' not in alternate_format.extension_attributes:
                e.append(['Alternate format url',
                          [alternate_format.type,alternate_format.url]])

    # show thumbnails
    if entry.media.thumbnail:
        for thumbnail in entry.media.thumbnail:
            e.append(['Thumbnail url',thumbnail.url])

    return e

standardfeed="http://gdata.youtube.com/feeds/api/standardfeeds/"

standardfeeds = ["most_viewed",
                 "top_rated",
                 "recently_featured",
                 "watch_on_mobile",
                 "most_discussed",
                 "top_favorites",
                 "most_linked",
                 "most_responded",
                 "most_recent",]

localeids = [
    ["Australia ","AU"],
    ["Brazil ","BR"],
    ["Canada ","CA"],
    ["Czech Republic ","CZ"],
    ["France ","FR"],
    ["Germany ","DE"],
    ["Great Britain ","GB"],
    ["Holland ","NL"],
    ["Hong Kong ","HK"],
    ["India ","IN"],
    ["Ireland ","IE"],
    ["Israel ","IL"],
    ["Italy ","IT"],
    ["Japan ","JP"],
    ["Mexico ","MX"],
    ["New Zealand ","NZ"],
    ["Poland ","PL"],
    ["Russia ","RU"],
    ["South Korea ","KR"],
    ["Spain ","ES"],
    ["Sweden ","SE"],
    ["Taiwan ","TW"],
    ["United States ","US"]]

def getstandardfeed(feed):
    return getfeed(standardfeed+feed)

def getstandardfeedlocale(feed,locale):
    return getfeed(standardfeed+locale+"/"+feed)

def getuserfeed(user):
    return getfeed("".join([
        "http://gdata.youtube.com/feeds/api/users/",
        user,"/uploads"]))

def getrelatedfeed(videoid):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    feed = yt_service.GetYouTubeRelatedVideoFeed(video_id=videoid)
    entries = []
    for entry in feed.entry:
        entries.append(entrydetails(entry))
    return entries

racy = ["include","exclude"]
orderyby = ["relevance","viewCount","published","rating"]
time = ["today","this_week","this_month","all_time"]

def search(search_terms,racy,maxresults,startindex,
           orderby,time,category,keywords,author):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    query = gdata.youtube.service.YouTubeVideoQuery()
    if author != "":
        query.author = author
    if category != "":
        query.categories.append(category)
    if keywords != []:
        for keyword in keywords:
            query.categories.append(keyword.lower())
    if search_terms != "":
        query.vq = search_terms
    if racy != "":
        query.racy = racy
    if maxresults != "":
        query.max_results = maxresults
    if startindex != "":
        query.start_index = startindex
    if orderby != "":
        query.orderby = orderby
    if time != "":
        query.time = time
    feed = yt_service.YouTubeQuery(query)
    entries = []
    for entry in feed.entry:
        entries.append(entrydetails(entry))
    return entries

def getcomments(videoid):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    comment_feed = yt_service.GetYouTubeVideoCommentFeed(video_id=videoid)
    comments = []
    for comment_entry in comment_feed.entry:
        comments.append(comment_entry.ToString())
    return comments

def getresponses(videoid):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    response_feed = yt_service.GetYouTubeVideoResponseFeed(video_id=videoid)
    responses = []
    for response in response_feed.entry:
        responses.append(response.ToString())
    return responses

def getplaylist(user):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    playlist_feed = yt_service.GetYouTubePlaylistFeed(username=user)
    videos = []
    for video in playlist_feed.entry:
        videos.append(video.ToString())
    return videos

# # a typical playlist URI
# playlist_uri = 'http://gdata.youtube.com/feeds/api/playlists/BCB3BB96DF51B505'

# playlist_video_feed = yt_service.GetYouTubePlaylistVideoFeed(uri=playlist_uri)

# # iterate through the feed as you would with any other
# for playlist_video_entry in playlist_video_feed.entry:
#   print playlist_video_entry.title.text

def authorlatest(author):
    return search("","","","","published","","","",author)

def authorlatestindex(author,startindex):
    return search("","","",str(startindex),"published","","","",author)

import time
def authorlatestall(author):
    i = 1
    t = time.time()
    total = 0
    while True:
        a = authorlatestindex(author,i)
        u.writepickle(a,"-".join(["/home/umar/youtubeauthor",
                                  author,str(i),str(t),str(time.time())]))
        n = len(a)
        total = total + n
        i = i + 25
        if n < 25:
            break
        if i > 1000:
            break
    print str(total)+" total videos"

