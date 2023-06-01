from logics.logic import Logic
from tests import data
def test_addUser(deleteUsers):
    response=Logic.addUser(data.user["user_name"],data.user["user_password"])
    assert response.status_code==200
    response=Logic.getUser(data.user["user_name"])
    assert response.status_code==200
    dataUser=data.user.copy()
    dataUser.pop("user_password")
    assert response.json()["data"]==dataUser

def test_addSong(deleteSongs):
    response=Logic.addSong(data.song["genre"],data.song["performer"],data.song["title"],data.song["year"])
    assert response.status_code==200
    response=Logic.getSong(data.song["title"])
    assert response.status_code==200
    assert response.json()["data"]==data.song

def test_add2UsersWithSameName(deleteUsers,addUser,addPlaylist):
    response=Logic.addUser(data.user["user_name"],data.user["user_password"]+"1")
    assert response.status_code==200
    response=Logic.getUser(data.user["user_name"])
    assert response.status_code==200
    assert response.json()["data"]["playlists"]!=[]

def test_downvoteSongWithRating0(deleteUsers,deleteSongs,addUser,addPlaylist,addSong,addSongToPlaylist):
    response=Logic.voteSong(False,data.playlist["playlist_name"],data.song["title"],data.user["user_name"],data.user["user_password"])
    assert response.status_code==200
    response=Logic.getSong(data.song["title"])
    assert response.status_code==200
    assert response.json()["data"]["rating"]==data.song["rating"]

def test_voteSongTwiceByUser(deleteUsers,deleteSongs,addUser,addPlaylist,addSong,addSongToPlaylist):
    response=Logic.voteSong(True,data.playlist["playlist_name"],data.song["title"],data.user["user_name"],data.user["user_password"])
    assert response.status_code==200
    response=Logic.voteSong(True,data.playlist["playlist_name"],data.song["title"],data.user["user_name"],data.user["user_password"])
    assert response.status_code==200
    response=Logic.getSong(data.song["title"])
    assert response.status_code==200
    assert response.json()["data"]["rating"]==data.song["rating"]+1