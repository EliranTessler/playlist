from flask import request
from flask_restx import Resource
from models import Playlist, Song, playlist_model, playlist_ns
from flask_jwt_extended import jwt_required
from exts import db

@playlist_ns.route('/playlists')
class PlaylistsResource(Resource):  
    @playlist_ns.marshal_list_with(playlist_model)
    def get(self):   
        playlists = Playlist.query.all()  
        return playlists

    @playlist_ns.marshal_with(playlist_model)
    @playlist_ns.expect(playlist_model) 
    @jwt_required()
    def post(self):
        data = request.get_json()
        name = data.get('name')
        song_names = data.get('songs', [])

        new_playlist = Playlist(name=name)

        try:
            db.session.add(new_playlist)
            db.session.commit()

            for song_name in song_names:
                new_song = Song(name=song_name, playlist_id=new_playlist.id)
                db.session.add(new_song)

            db.session.commit()

            serialized_playlist = marshal(new_playlist, playlist_model)
            return serialized_playlist, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the playlist", "error": str(e)}, 500
     
@playlist_ns.route('/playlist/<int:id>')
class PlaylistResource(Resource):

    @playlist_ns.marshal_with(playlist_model)
    @jwt_required()
    def get(self, id):
        playlist=Playlist.query.get_or_404(id)

        return playlist

    @playlist_ns.marshal_with(playlist_model) 
    @jwt_required()
    def put(self, id):
        playlist=Playlist.query.get_or_404(id)
        data=request.get_json()

        playlist.update(data.get('name'))

        return playlist 


    @playlist_ns.marshal_with(playlist_model)
    @jwt_required()  
    def delete(self, id):
        playlist=Playlist.query.get_or_404(id)

        playlist.delete()

        return playlist
    
@playlist_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
            return {"message":"Hello World"}
    
 