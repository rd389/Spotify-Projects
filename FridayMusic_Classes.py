import spotipy
import datetime

class FavArtists(object):
    """ Information about one's favorite Spotify artists:

    Attributes:
        artists: List of strings containing favorite artist URIs.
        new_music: List of URIS of new albums released by favorite artists.
    """
    
    def __init__(self, fav_artists=[]):
        if fav_artists == []:
            artists = []
            a = raw_input('Please enter the exact names of one of your favorite artists, or END: ')
            while a != 'END':
                artists.append(a)
                a = raw_input('Enter another artist\'s exact name, or END: ')
            spotify = spotipy.Spotify()
        else:
            artists = fav_artists
        uris = []
        spotify = spotipy.Spotify() 
        for artist in artists:
            artist_uri = spotify.search(q=artist,limit=1,type='artist')['artists']['items'][0]['uri']
            uris.append(artist_uri)
        self.artists = uris
        new_music = []
        for uri in uris:
            for artist_album in spotify.artist_albums(uri)['items']:
                try:    
                    album_uri = artist_album['uri']
                    album = spotify.album(album_uri)
                    album_release = album['release_date'].split('-')
                    release_date = datetime.date(int(album_release[0]), int(album_release[1]), int(album_release[2]))
                    last_week = datetime.date.today() - datetime.timedelta(days=7)
                    if release_date > last_week:
                        new_music.append(album_uri)
                except IndexError:
                    continue
        self.new_music = new_music
        
class MySpotify(object):
    """ Information about a user's Spotify account:
    
    Attributes:
        TBD
    """
