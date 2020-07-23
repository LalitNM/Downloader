def MakeName(url):
    slash = []
    # insert last slash
    slash.insert(0, url.rfind('/'))
    # insert second last slash
    slash.insert(0, url.rfind('/', 0, slash[-1]))
    # insert third slash
    slash.insert(0, url.rfind('/', 0, slash[-2]))
    name = url[slash[-1] + 1:]
    name = "".join(name.split("%20"))
    album = url[slash[-2] + 1:slash[-1]]
    album = "".join(album.split("%20"))
    album = album[:album.find("%")]
    year = url[slash[-3] + 1:slash[-2]]
    return year, album, name

def CleanName(name):
    return name.replace("%20", "_")

def FindLinks(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = str(urlopen(req).read())
    soup = BeautifulSoup(webpage, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True, text=True):
        last_slash = a['href'].rfind("/")
        second_last_slash = a['href'].rfind("/", 0, last_slash)
        if a['href'][-1] == "/":
            links.append(a['href'][second_last_slash + 1:])
        else:
            links.append(a['href'][last_slash + 1:])
    return links[5:]
