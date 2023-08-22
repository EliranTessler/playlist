from flask import Flask
from flask_restx import Api, Resource
from models import Playlist, Song, User
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from playlists import playlist_ns
from songs import songs_ns
from auth import auth_ns
from config import TestConfig
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, origins=['http://localhost:3000'])

    if config is not TestConfig:
        db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    JWTManager(app)

    api=Api(app, doc='/docs')

    api.add_namespace(playlist_ns)
    api.add_namespace(songs_ns)
    api.add_namespace(auth_ns)

    @api.route('/hello')
    class HelloResource(Resource):
        def get(self):
            return {"message":"Hello World"}, 201

    @app.shell_context_processor
    def make_shell_context():
     return {
          "db": db,
          "Playlist":Playlist,
          "Song":Song,
          "User":User
     }
    
    return app
    