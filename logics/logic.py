from infra.restSender import RestSender
class Logic:
    baseUrl="http://127.0.0.1:3002"
    userUrl=baseUrl+"/users"
    songUrl=baseUrl+"/songs"
    playlistUrl=baseUrl+"/playlists"
    adminUrl=baseUrl+"/admin"
    @staticmethod
    def getUser(name):
        url=Logic.userUrl+"/get_user"
        params={
            "user_name":name
        }
        return RestSender.sendGetMsg(url,params)
    @staticmethod
    def addUser(name,password):
        url=Logic.userUrl+"/add_user"
        data={
            "user_name":name,
            "user_password":password
        }
        return RestSender.sendPostMsg(url,data)
    @staticmethod
    def addPlaylist(name,userName,userPassword):
        url=Logic.userUrl+"/add_playlist"
        data={
            "playlist_name":name,
            "user_name":userName,
            "user_password":userPassword
        }
        return RestSender.sendPostMsg(url,data)
    @staticmethod
    def getSong(title):
        url=Logic.songUrl+"/get_song"
        params={
            "song_title":title
        }
        return RestSender.sendGetMsg(url,params)
    @staticmethod
    def addSong(genre,performer,title,year):
        url=Logic.songUrl+"/add_song"
        data={
            "song_genre":genre,
            "song_performer":performer,
            "song_title":title,
            "song_year":year
        }
        return RestSender.sendPostMsg(url,data)
    @staticmethod
    def voteSong(up,playlistName,songTitle,userName,userPassword):
        url=Logic.songUrl+("/upvote" if up else "/downvote")
        data={
            "playlist_name":playlistName,
            "song_title":songTitle,
            "user_name":userName,
            "user_password":userPassword
        }
        return RestSender.sendPutMsg(url,data)
    @staticmethod
    def addSongToPlaylist(playlistName,songTitle,userName,userPassword):
        url=Logic.playlistUrl+"/add_song"
        data={
            "playlist_name":playlistName,
            "song_title":songTitle,
            "user_name":userName,
            "user_password":userPassword
        }
        return RestSender.sendPostMsg(url,data)
    @staticmethod
    def deleteUsers():
        url=Logic.adminUrl+"/delete_all_users"
        return RestSender.sendDeleteMsg(url)
    @staticmethod
    def deleteSongs():
        url=Logic.adminUrl+"/delete_all_songs"
        return RestSender.sendDeleteMsg(url)