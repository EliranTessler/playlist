from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_restful import marshal
from config import DevConfig
from models import Playlist, Song
from sqlalchemy.sql import exists    
from exts import db
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate=Migrate(app, db)
migrate.init_app(app, db)

api=Api(app, doc='/docs')

song_model=api.model(
    "Song",
    {
       "id":fields.Integer(),
       "name":fields.String(),
       "playlist_id":fields.Integer()
    }
)

playlist_model=api.model(
     "Playlist",
     {
        "id":fields.Integer(), 
        "name":fields.String(),
        "songs":fields.List(fields.Nested(song_model))
     }
)


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
            return {"message":"Hello World"}
    

@api.route('/playlists')
class PlaylistsResource(Resource):  
    @api.marshal_list_with(playlist_model)
    def get(self):   
        playlists=Playlist.query.all()  
        return playlists

    @api.expect(playlist_model) 
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
     
@api.route('/playlist/<int:id>')
class PlaylistResource(Resource):

    @api.marshal_with(playlist_model)
    def get(self, id):
        playlist=Playlist.query.get_or_404(id)

        return playlist

    @api.marshal_with(playlist_model) 
    def put(self, id):
        playlist=Playlist.query.get_or_404(id)
        data=request.get_json()

        playlist.update(data.get('name'))

        return playlist 


    @api.marshal_with(playlist_model)  
    def delete(self, id):
        playlist=Playlist.query.get_or_404(id)

        playlist.delete()

        return playlist
    

@api.route('/songs/<int:id>')
class SongResource(Resource):

    @api.marshal_with(song_model)
    def get(self, id):
        song=Song.query.get_or_404(id)

        return song

    @api.marshal_with(song_model) 
    def put(self, id):
        song=Song.query.get_or_404(id)
        data=request.get_json()

        song.update(data.get('name'))

        return song 

    @api.marshal_with(playlist_model)  
    def delete(self, id):
        song=Song.query.get_or_404(id)

        song.delete()

        return song    

    @api.expect(song_model) 
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
                 
@app.shell_context_processor
def make_shell_context():
     return {
          "db": db,
          "Playlist":Playlist
     }

if __name__ == '__main__':
    app.run()