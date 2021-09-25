from os import system

import spotipy
from pycenter import center
from pystyle import Colorate, Colors
from spotipy.oauth2 import SpotifyClientCredentials
from treelib import Tree


class spotipymain:
    def __init__(self):
        system("cls")
        self.title = """
        
.▄▄ ·  ▄▄▄·      ▄▄▄▄▄▪  .▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
▐█ ▀. ▐█ ▄█▪     •██  ██ ▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
▄▀▀▀█▄ ██▀· ▄█▀▄  ▐█.▪▐█·▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█
▐█▄▪▐█▐█▪·•▐█▌.▐▌ ▐█▌·▐█▌▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀
 ▀▀▀▀ .▀    ▀█▄▀▪ ▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·
 
                    By Kijusu / Maxence
                
        (01) Username to ID | (02) Search with ID

        """

        print(Colorate.Horizontal(Colors.blue_to_cyan, center(self.title)))

        while True:
            self.choice = input(f"{Colorate.Color(Colors.cyan, 'SpotiSearch -> ')}")
            if self.choice == '01':
                spotipysearchUSER()
            if self.choice == '02':
                spotipysearchID().resultsSearch()


class spotipysearchUSER:
    def __init__(self):
        self.name = input("\nName of artist -> ")
        self.clientID = "24f5b30de8fc4bc2b53d5a3b5e51ee6e"
        self.secretID = "ecc50ad105d545f2b4c65c0e6316739f"
        self.connect_spotify =  spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(self.clientID, self.secretID))
        self.results = self.connect_spotify.search(q="artist:" + self.name, type='artist')

        self.r = None
        self.items = self.results['artists']['items']
        if len(self.items) > 0:
            self.r = self.items[0]
            print("ID : "+self.r['id'], '\n')

class spotipysearchID:
    def __init__(self):
        system("cls")
        self.title = """
        
.▄▄ ·  ▄▄▄·      ▄▄▄▄▄▪  .▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
▐█ ▀. ▐█ ▄█▪     •██  ██ ▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
▄▀▀▀█▄ ██▀· ▄█▀▄  ▐█.▪▐█·▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█
▐█▄▪▐█▐█▪·•▐█▌.▐▌ ▐█▌·▐█▌▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀
 ▀▀▀▀ .▀    ▀█▄▀▪ ▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·
 
                    By Kijusu / Maxence

        """

        print(Colorate.Horizontal(Colors.blue_to_cyan, center(self.title)))

        self.id = input(f"{Colorate.Color(Colors.cyan, 'Artists ID -> ')}")
        self.clientID = "24f5b30de8fc4bc2b53d5a3b5e51ee6e"
        self.secretID = "ecc50ad105d545f2b4c65c0e6316739f"
        self.connect_spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(self.clientID, self.secretID))
        self.results = self.connect_spotify.artist_top_tracks(f'spotify:artist:{self.id}')

        self.tree = Tree()
        self.treeInfo = Tree()
        self.treeAlbums = Tree()
        self.treeUrlAlbums = Tree()

        self.r = None
        self.number = None

    def resultsSearch(self):

        for self.r in self.results['tracks'][:1]:
            self.tree.create_node(f"\n{Colorate.Color(Colors.blue, self.r['artists'][0]['name'])}", 1)

        self.treeAlbums.create_node(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Album on Spotify')}", 2)
        self.treeUrlAlbums.create_node(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Album image URL')}", 4)

        for self.r in self.results['tracks']:
            self.treeAlbums.create_node(self.r['name'], parent=2)
            self.treeUrlAlbums.create_node(self.r['album']['images'][0]['url'], parent=4)

        self.treeInfo.create_node(f"{Colorate.Horizontal(Colors.blue_to_cyan, 'Information Spotify')}", 3)
        self.treeInfo.create_node(f"Id : {self.r['artists'][0]['id']}", parent=3)
        self.treeInfo.create_node(f"Type : {self.r['artists'][0]['type']}", parent=3)
        self.treeInfo.create_node(f"Uri : {self.r['artists'][0]['uri']}", parent=3)
        self.treeInfo.create_node(f"Name : {self.r['artists'][0]['name']}", parent=3)
        self.treeInfo.create_node(f"Spotify url : https://open.spotify.com/artist/{self.id}", parent=3)

        self.tree.paste(1, self.treeAlbums)
        self.tree.paste(1, self.treeInfo)
        self.tree.paste(1, self.treeUrlAlbums)

        self.tree.show(line_type="ascii-em")

        returnMain = input(f"{Colorate.Color(Colors.cyan, 'Replay (Y or N) -> ')}")

        if returnMain.lower()[0:1] == 'y':
            exit()
        if returnMain.lower()[0:1] == 'n':
            spotipymain()


spotipymain()

# 58wXmynHaAWI5hwlPZP3qL
# https://open.spotify.com/artist/58wXmynHaAWI5hwlPZP3qL
