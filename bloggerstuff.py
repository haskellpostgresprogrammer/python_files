from gdata import service
import gdata
import atom
import umarutils as u

def clientlogin(appname,servicename,server):
    password = u.getpass()
    blogger_service = service.GDataService(password[0],
                                           password[1])
    blogger_service.ssl = True
    blogger_service.source = appname
    blogger_service.service = servicename
    blogger_service.account_type = 'GOOGLE'
    blogger_service.server = server
    blogger_service.ProgrammaticLogin()
    return blogger_service

def bloggerlogin(appname):
    return clientlogin(appname,
                       "blogger","www.blogger.com")

def blogtitles(appname):
    blogger_service = bloggerlogin(appname)
    query = service.Query()
    query.feed = '/feeds/default/blogs'
    feed = blogger_service.Get(query.ToUri())
    return [feed.title.text,
            [[x.title.text,x.GetSelfLink().href.split("/")[-1]]
             for x in feed.entry]]

def blogposts(blog_id,appname,
              categories,max_results,start_index,
              published_min,published_max,
              updated_min,updated_max):
    blogger_service = bloggerlogin(appname)
    query = service.Query()
    query.feed = "/feeds/" + blog_id + "/posts/default"

    if categories != "":
        query.categories = categories
    if start_index != "":
        query.start_index = str(start_index)
    if max_results != "":
        query.max_results = str(max_results)
    if published_min != "":
        query.published_min = "-".join(published_min)
    if published_max != "":
        query.published_max = "-".join(published_max)
    if updated_min != "":
        query.updated_min = "-".join(updated_min)
    if updated_max != "":
        query.updated_max = "-".join(updated_max)

    feed = blogger_service.GetFeed(query.ToUri())
    data = []
    data.append(feed.title.text)
    for entry in feed.entry:
        e = []
        if entry.title.text:
            e.append(entry.title.text)
        if entry.content.text:
            e.append(entry.content.text)
        if entry.updated.text:
            e.append(entry.updated.text)
        if entry.GetEditLink().href:
            e.append(entry.GetEditLink().href)
        data.append(e)
    return data

def blogid(name):
    t = blogtitles("app1")[1]
    return [x[1] for x in t if x[0] == name][0]

def blogpostslatest(blogid,start_index):
    return blogposts(blogid,"app1","","",start_index,"","","","")

def createpublicpost(blogid, title, content):
    blogger_service = bloggerlogin("app1")
    blog_id = blogid
    entry = gdata.GDataEntry()
    entry.title = atom.Title('xhtml', title)
    entry.content = atom.Content(content_type='html', text=content)
    blogger_service.Post(entry, '/feeds/%s/posts/default' % blog_id)

def updatepost(title,content,editlink):
    blogger_service = bloggerlogin("app1")
    entry = gdata.GDataEntry()
    entry.title = atom.Title('xhtml', title)
    entry.content = atom.Content(content_type='html', text=content)
    blogger_service.Put(entry,editlink)

def deletepost(editlink):
    blogger_service = bloggerlogin("app1")
    blogger_service.Delete(editlink)

# def CreateComment(blogger_service,
#                   blog_id, post_id, comment_text='Mostly harmless'):
#     feed_uri = '/feeds/' + blog_id + '/' + post_id + '/comments/default'
#     entry = gdata.GDataEntry()
#     entry.content = atom.Content(content_type='xhtml',
#                                  text=comment_text)
#     return blogger_service.Post(entry, feed_uri)

# def PrintAllComments(blogger_service, blog_id, post_id):
#     feed_url = '/feeds/' + blog_id + '/' + post_id + '/comments/default'
#     feed = blogger_service.Get(feed_url)

#     print feed.title.text
#     for entry in feed.entry:
#         print "\t" + entry.title.text
#         print "\t" + entry.updated.text
#     print 

# Or you can get the comments from all posts by using the blog's comments feed URL:
# http://www.blogger.com/feeds/blogID/comments/default

# def DeleteComment(blogger_service, post_id, comment_id):
#     feed_url = '/feeds/' + post_id + '/comments/default/' + comment_id
#     blogger_service.Delete(feed_url)

# incomplete
