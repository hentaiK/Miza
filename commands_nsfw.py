import nekos,discord,urllib
from smath import *

image_forms = [
    "gif",
    "png",
    "bmp",
    "jpg",
    "jpeg",
    "tiff",
    ]
class urlBypass(urllib.request.FancyURLopener):
    version = "Mozilla/5."+str(xrand(1,10))
def pull_e621(argv,delay=5):
    opener = urlBypass()
    items = argv.replace(" ","%20").lower()
    baseurl = "https://e621.net/post/index/"
    url = baseurl+"1/"+items
    resp = opener.open(url)
    if resp.getcode() != 200:
        raise ConnectionError("Error "+str(resp.getcode()))
    s = resp.read().decode("utf-8")

    ind = s.index('class="next_page" rel="next"')
    s = s[ind-90:ind]
    d = s.split(" ")
    i = -1
    while True:
        if "</a>" in d[i]:
            break
        i -= 1
    u = d[i][:-4]
    u = u[u.index(">")+1:]
    v1 = xrand(1,int(u))

    url = baseurl+str(v1)+"/"+items
    resp = opener.open(url)
    if resp.getcode() != 200:
        raise ConnectionError("Error "+str(resp.getcode()))
    s = resp.read().decode("utf-8")

    try:
        limit = s.index('class="next_page" rel="next"')
        s = s[:limit]
    except:
        pass

    search = '<a href="/post/show/'
    sources = []
    while True:
        try:
            ind1 = s.index(search)
            s = s[ind1+len(search):]
            ind2 = s.index('"')
            target = s[:ind2]
            try:
                sources.append(int(target))
            except:
                pass
        except:
            break
    x = None
    while not x:
        v2 = xrand(len(sources))
        x = sources[v2]
        found = False
        for i in image_forms:
            if i in x:
                found = True
        if not found:
            x = None
    url = "https://e621.net/post/show/"+str(x)
    resp = opener.open(url)
    if resp.getcode() != 200:
        raise ConnectionError("Error "+str(resp.getcode()))
    s = resp.read().decode("utf-8")

    search = '<a href="https://static1.e621.net/data/'
    ind1 = s.index(search)
    s = s[ind1+9:]
    ind2 = s.index('"')
    s = s[:ind2]
    url = s
    return [url,v1,v2]

def pull_rule34(argv,delay=5):
    items = argv.split("_")
    for i in range(len(items)):
        items[i] = items[i][0].upper()+items[i][1:].lower()
    items = "_".join(items)
    items = argv.split(" ")
    for i in range(len(items)):
        items[i] = items[i][0].upper()+items[i][1:]
    items = "%20".join(items)
    baseurl = "https://rule34.paheal.net/post/list/"
    try:
        url = baseurl+items+"/1"
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req,timeout=delay)
    except:
        url = baseurl+items.upper()+"/1"
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req,timeout=delay)
    if resp.getcode() != 200:
        raise ConnectionError("Error "+str(resp.getcode()))
    
    s = resp.read().decode("utf-8")
    try:
        ind = s.index('">Last</a><br>')
        s = s[ind-5:ind]
        v1 = xrand(1,int(s.split("/")[-1]))
        url = url[:-1]+str(v1)
        
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req,timeout=delay)
        if resp.getcode() != 200:
            raise ConnectionError("Error "+str(resp.getcode()))
        s = resp.read().decode("utf-8")
    except:
        pass
    try:
        limit = s.index("class=''>Images</h3><div class='blockbody'>")
        s = s[limit:]
        limit = s.index("</div></div></section>")
        s = s[:limit]
    except:
        pass

    search = 'href="'
    sources = []
    while True:
        try:
            ind1 = s.index(search)
            s = s[ind1+len(search):]
            ind2 = s.index('"')
            target = s[:ind2]
            if not "." in target:
                continue
            elif ".js" in target:
                continue
            found = False
            for i in image_forms:
                if i in target:
                    found = True
            if target[0]=="h" and found:
                sources.append(target)
        except:
            break
    v2 = xrand(len(sources))
    url = sources[v2]
    return [url,v1,v2]

def searchRandomNSFW(argv,delay=10):
    nsfw = {
        0:pull_rule34,
        1:pull_e621,
        }
    data = None
    while True:
        l = list(nsfw)
        if not l:
            break
        r = xrand(len(l))
        try:
            f = nsfw[r]
            nsfw.pop(r)
        except:
            break
        try:
            data = f(argv,delay/2)
        except:
            continue
        break
    if data is None:
        raise EOFError("Unable to locate any search results.")
    return data

neko_tags = {
    "feet":True,
    "yuri":True,
    "trap":True,
    "futanari":True,
    "hololewd":True,
    "lewdkemo":True,
    "solog":True,
    "feetg":True,
    "cum":True,
    "erokemo":True,
    "les":True,
    "wallpaper":True,
    "lewdk":True,
    "ngif":False,
    "tickle":False,
    "lewd":True,
    "feed":False,
    "gecg":False,
    "eroyuri":True,
    "eron":True,
    "cum_jpg":True,
    "bj":True,
    "nsfw_neko_gif":True,
    "solo":True,
    "kemonomimi":True,
    "nsfw_avatar":True,
    "gasm":False,
    "poke":False,
    "anal":True,
    "slap":False,
    "hentai":True,
    "avatar":False,
    "erofeet":True,
    "holo":True,
    "keta":True,
    "blowjob":True,
    "pussy":True,
    "tits":True,
    "holoero":True,
    "lizard":False,
    "pussy_jpg":True,
    "pwankg":True,
    "classic":True,
    "kuni":True,
    "waifu":False,
    "pat":False,
    "8ball":False,
    "kiss":False,
    "femdom":True,
    "neko":False,
    "spank":True,
    "cuddle":False,
    "erok":True,
    "fox_girl":False,
    "boobs":True,
    "random_hentai_gif":True,
    "smallboobs":True,
    "hug":False,
    "ero":True,
    "smug":False,
    "goose":False,
    "baka":False,
    "cat":False,
    "gif":False,
    }
def is_nsfw(channel):
    try:
        return channel.is_nsfw()
    except AttributeError:
        return True
class neko:
    is_command = True
    def __init__(self):
        self.name = []
        self.minm = 1
        self.desc = "Pulls a random image from nekos.life and embeds it."
        self.usag = '<tags:[](?r)> <verbose:(?v)> <list:(?l)>'
    async def __call__(self,args,flags,channel,**void):
        isNSFW = is_nsfw(channel)
        if "l" in flags:
            text = "Available commands in **#"+channel.name+"**:\n`"
            for key in neko_tags:
                if isNSFW or not neko_tags[key]:
                    text += key+", "
            text = text[:-2]+"`"
            return text
        tagNSFW = False
        selected = []
        for tag in args:
            tag = tag.replace(",","").lower()
            if tag in neko_tags:
                if neko_tags.get(tag,0):
                    tagNSFW = True
                    if not isNSFW:
                        raise PermissionError("Error: This command is only available in NSFW channels.")
                selected.append(tag)
        for x in range(flags.get("r",0)):
            possible = [i for i in neko_tags if neko_tags[i]<=isNSFW]
            selected.append(possible[xrand(len(possible))])
        if not selected:
            url = nekos.img("neko")
        else:
            v = xrand(len(selected))
            get = selected[v]
            if get == "gif":
                if tagNSFW:
                    url = nekos.img("nsfw_neko_gif")
                else:
                    url = nekos.img("ngif")
            elif get == "cat":
                url = nekos.cat()
            else:
                url = nekos.img(get)
        if "v" in flags:
            text = "Pulled from "+url
            return text
        else:
            emb = discord.Embed(url=url)
            emb.set_image(url=url)
            print(url)
            await channel.send(embed=emb)

class lewd:
    is_command = True
    def __init__(self):
        self.name = ["nsfw"]
        self.minm = 1
        self.desc = "Pulls a random image from a search on Rule34 and e621, and embeds it."
        self.usag = '<query> <verbose:(?v)>'
    async def __call__(self,_vars,args,flags,channel,**void):
        if not is_nsfw(channel):
            raise PermissionError("Error: This command is only available in NSFW channels.")
        objs = searchRandomNSFW(" ".join(args),_vars.timeout)
        url = objs[0]
        if "v" in flags:
            text = "Pulled from "+url+"\nImage **__"+str(objs[2])+"__** on page **__"+str(objs[1])+"__**"
            return text
        else:
            emb = discord.Embed(url=url)
            emb.set_image(url=url)
            print(url)
            await channel.send(embed=emb)

class owoify:
    is_command = True
    def __init__(self):
        self.name = ["owo"]
        self.minm = 0
        self.desc = "owo-ifies text."
        self.usag = '<string>'
    async def __call__(self,argv,**void):
        return "```\n"+nekos.owoify(argv)+"```"