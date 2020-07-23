import requests
import os

from helper import *

base = "https://pagaldownload.info/Bollywood/"

years = FindLinks(base)

for year in years:
    print(year, end = " ")
year = input("\n\nThese are available options, please type any one: ")
year += "/"
raw_albums = FindLinks(base + year)
albums = [CleanName(i) for i in raw_albums]
lengthy_album = ""
for i in albums:
    if len(i) > len(lengthy_album):
        lengthy_album = i
max_len = len(lengthy_album)

print("\n\n")

for album in albums:
    print(CleanName(album) + " "*(max_len-len(album)), albums.index(album))

print("\n\n")

album_index = int(input("Enter index of album whose songs you want to download: "))
album = raw_albums[album_index]

raw_songs = FindLinks(base + year + album)
print(raw_songs)
print("\n\n")

for i in raw_songs:
    print(CleanName(i))

print("\n\nThese songs will be downloaded, do you want to continue?(y/n): ", end = "")
agree = input()

# make directories:
if "downloads" not in os.listdir():
    os.mkdir("downloads/")

os.chdir("downloads/")
if "songs" not in os.listdir():
    os.mkdir("songs")

os.chdir("songs")

if year[:-1] not in os.listdir():
    os.mkdir(year[:-1])
os.chdir(year[:-1])

if CleanName(album)[:-1] not in os.listdir():
    os.mkdir(CleanName(album))
os.chdir(CleanName(album))

print(os.getcwd())

if agree == "y":
    for song in raw_songs:
        r = requests.get(base + year + album + song, allow_redirects=True)
        print("Downloading " + CleanName(song))
        open(CleanName(song), 'wb').write(r.content)
elif agree == "n":
    print("Ok, We will not download them.")
else:
    print("You did\"t entered \"y\" or \"n\"")
# print(MakeName(url))
# os.mkdir("songs")
# os.chdir("songs")
