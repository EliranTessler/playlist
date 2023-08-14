from flask import request
from flask_restx import Resource
from models import Playlist, Song, song_model, songs_ns, playlist_model
from exts import db

@songs_ns.route('/songs/<int:id>')
class SongResource(Resource):

    @songs_ns.marshal_with(song_model)
    def get(self, id):
        song=Song.query.get_or_404(id)

        return song

    @songs_ns.marshal_with(song_model) 
    def put(self, id):
        song=Song.query.get_or_404(id)
        data=request.get_json()

        song.update(data.get('name'))

        return song 

    @songs_ns.marshal_with(playlist_model)  
    def delete(self, id):
        song=Song.query.get_or_404(id)

        song.delete()

        return song    

    @songs_ns.expect(song_model) 
    def post(self, id):

        exists = db.session.query(Playlist.id).filter_by(id=id).first() is not None

        if exists:
            data = request.get_json()
            name = data.get('name')

            new_song = Song(name=name, playlist_id=id)

            try:
                db.session.add(new_song)
                db.session.commit()

                serialized_playlist = marshal(new_song, song_model)
                return serialized_playlist, 201
            except Exception as e:
                db.session.rollback()
                return {"message": "An error occurred while creating the playlist", "error": str(e)}, 500
        else:
            return {"message": "Playlist ID invalid."}, 405