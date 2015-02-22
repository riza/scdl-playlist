#!/usr/bin/python
#-*- coding: utf-8 -*-
import os

try:
    import requests
except ImportError, e:
    print u"Lütfen requests modülünü kurun!"
    exit()
# şu alt tarafı yusuf(kulturlupenguen) karrrdeşimden copy paste yaptım :(
print "#=============================================#"
print "#                                             #"
print "#    	 Soundcloud Playlist Downloader      #"
print "#        	    Rıza Sabuncu                 #"
print "#                                             #"
print "#---------------------------------------------#"
print "#                                             #"
print "#       twitter  : rizasabuncu                #"
print "#       facebook : dentrimental.sh            #"
print "#       github   : rizasabuncu                #"
print "#       blog     : 32byte.org                 #"
print "#                                             #"
print "#---------------------------------------------#"
print
print
print

API_KEY = "" # http://32byte.org/soundcloud-playlist-indirme-python/
URL = raw_input("Playlist linki giriniz : ")
API_LINK = 'http://api.soundcloud.com/resolve.json?url=' + URL + '&client_id=' + API_KEY

r = requests.get(API_LINK)
data = r.json()

playlistName = data["title"] + ""

if not os.path.exists(playlistName):
	os.mkdir(playlistName)

BASE_PATH = os.path.abspath(os.path.dirname(__file__)) + "/" + playlistName


for tracks in data["tracks"]:
	parcaAdi = tracks["title"]

	print parcaAdi + " indiriliyor.."
	streamData = tracks["stream_url"] + "?client_id=" + API_KEY

	path = os.path.join(BASE_PATH, '{0:s}.mp3'.format(tracks["permalink"]))

	data = requests.get(streamData, stream=True)

	with open(path, 'wb+') as f:
	    for chunk in data.iter_content(chunk_size=32*1024):
	        if chunk:
	            f.write(chunk)
	            f.flush()

print playlistName + " indirildi."
print "Feedback : rizasabuncu"



