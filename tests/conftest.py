from pytest import fixture
from logics.logic import Logic
from tests import data
@fixture()
def deleteUsers():
    Logic.deleteUsers()
@fixture()
def deleteSongs():
    Logic.deleteSongs()
@fixture()
def addUser():
    Logic.addUser(data.user["user_name"],data.user["user_password"])
@fixture()
def addPlaylist():
    Logic.addPlaylist(data.playlist["playlist_name"],data.user["user_name"],data.user["user_password"])
@fixture()
def addSong():
    Logic.addSong(data.song["genre"],data.song["performer"],data.song["title"],data.song["year"])
@fixture()
def addSongToPlaylist():
    Logic.addSongToPlaylist(data.playlist["playlist_name"],data.song["title"],data.user["user_name"],data.user["user_password"])