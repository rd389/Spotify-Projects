import spotipy
import spotipy.util as util
import schedule
from FridayMusic_Classes import FavArtists as fa

def save_new_music():
    client_id = 'b3c8b17bdc094b9385704b61d009bb79'
    redirect_uri = 'http://localhost/'
    scope = 'user-library-modify'
    user_id = raw_input('Please enter your Spotify User ID #: ')
    client_secret = raw_input('Please enter Friday Music application\'s client secret: ')
    token = util.prompt_for_user_token(user_id, scope=scope, client_id=client_id, client_secret = client_secret, redirect_uri = redirect_uri)
    
    if token:
        sp = spotipy.Spotify(auth=token)
        your_artists = fa()
        if len(your_artists.new_music) > 0:
            sp.current_user_saved_albums_add(your_artists.new_music)
    
# work on scheduling task

save_new_music()