from flask import Flask
from flask_restx import Api
from models import Playlist, Song, User
from sqlalchemy.sql import exists    
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from playlists import playlist_ns
from songs import songs_ns
from auth import auth_ns


def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    migrate=Migrate(app, db)
    migrate.init_app(app, db)
    JWTManager(app)

    api=Api(app, doc='/docs')

    api.add_namespace(playlist_ns)
    api.add_namespace(songs_ns)
    api.add_namespace(auth_ns)

    @app.shell_context_processor
    def make_shell_context():
     return {
          "db": db,
          "Playlist":Playlist,
          "Song":Song,
          "User":User
     }
    
    return app
    