import umarutils as u
import youtubestuff as yt
import postgrescommands as pg
import psycopg2 as p

def downloadyoutubevideo(video):
    return u.shellcommand(
        ["/home/umar/youtube-dl",video])

# def youtube2db(data,searchterms,racy,orderby,
#                timelimit,scategory,keywords,author,
#                startindex):
#     conn = p.connect(pg.mypersonal())
#     cur = conn.cursor()
#     for video in data:
#         yid = [x[1] for x in video if x[0] == "id"][0]
#         for field in video:
#             cur.execute("""
#             insert into youtube.data (yid,field,value,
#             searchterms,racy,orderby,
#             timelimit,scategory,keywords,author,
#             startindex) values (%s,%s,%s,%s,%s,
#             %s,%s,%s,%s,%s,%s);
#             """,[yid,field[0],field[1],searchterms,
#                  racy,orderby,timelimit,scategory,
#                  keywords,author,startindex])
#     conn.commit()
#     conn.close()
#     return

def field2string(field,video):
    for item in video:
        if item[0] == field:
            value = item[1]
            if field == "Alternate format url":
                values = [x[1] for x in video
                          if x[0] == "Alternate format url"]
                return "\n".join(["\t".join(x) for x in values])
            elif field == "Thumbnail url":
                values = [x[1] for x in video
                          if x[0] == "Thumbnail url"]
                return "\n".join(values)
            elif field == "Video geo location":
                return "\n".join(item[1])
            elif isinstance(value,str):
                return value                
            elif value == None:
                return ""
        
def youtube2db(data,searchterms,racy,orderby,
               timelimit,scategory,keywords,author,
               startindex):
    conn = p.connect(pg.mypersonal())
    cur = conn.cursor()
    for video in data:
        yid = field2string("id",video)
        flashurl = field2string("Video flash player URL",
                                video)
        duration = field2string("Video duration",video)
        title = field2string("Video title",video)
        description = field2string("Video description",
                                   video)
        watchpage = field2string("Video watch page",
                                 video)
        geolocation = field2string("Video geo location",video)
        alternateformats = field2string("Alternate format url",video)
        viewcount = field2string("Video view count",
                                 video)
        rating = field2string("Video rating",video)
        publishedon = field2string("Video published on",video)
        category = field2string("Video category",video)
        thumbnails = field2string("Thumbnail url",video)
        cur.execute("""
        insert into youtube.data
        (yid,flashurl,duration,title,description,
        watchpage,alternateformats,
        viewcount,rating,publishedon,category,
        thumbnails,searchterms,racy,orderby,
        timelimit,scategory,keywords,author,
        startindex,geolocation)
        values (%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s);
        """,[yid,flashurl,duration,title,description,
             watchpage,alternateformats,
             viewcount,rating,publishedon,category,
             thumbnails,searchterms,racy,orderby,
             timelimit,scategory,keywords,author,
             str(startindex),geolocation])
#         l.append([yid,flashurl,duration,title,description,
#                   watchpage,alternateformats,
#                   viewcount,rating,publishedon,category,
#                   thumbnails,searchterms,racy,orderby,
#                   timelimit,scategory,keywords,author,
#                   str(startindex),geolocation])
    conn.commit()
    conn.close()
    return 

def ytq2db1000(searchterms,racy,orderby,
               timelimit,category,keywords,author):
    reslength = 25
    for startindex in range(1,1001,25):
        res = yt.search(searchterms,racy,
                        "25",str(startindex),
                        orderby,timelimit,category,
                        keywords,author)
        print startindex," ",len(res)
        reslength = len(res)
        if reslength == 0:
            print "ended"
            break
        else:
            youtube2db(res,searchterms,racy,orderby,
                       timelimit,category,keywords,author,
                       startindex)
    return

def ytq2db25(searchterms,racy,orderby,
             timelimit,category,keywords,author):
    startindex = 1
    res = yt.search(searchterms,racy,
                    "25",str(startindex),
                    orderby,timelimit,category,
                    keywords,author)
    youtube2db(res,searchterms,racy,orderby,
               timelimit,category,keywords,author,
               startindex)

def search2db1000(searchterms):
    ytq2db1000(searchterms,"","","","","","")
def author2db1000(author):
    ytq2db1000("","","published","","","",author)
def search2db25(searchterms):
    ytq2db25(searchterms,"","","","","","")
def author2db25(author):
    ytq2db25("","","published","","","",author)
def search2db25latest(searchterms):
    ytq2db25(searchterms,"","published","","","","")

