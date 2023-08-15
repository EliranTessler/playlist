from exts import db
from sqlalchemy import ForeignKey
from flask_restx import fields, Namespace

playlist_ns = Namespace('playlist', description="A namespace for Playlist")
auth_ns = Namespace('auth', description="A namespace for Authentication")
songs_ns = Namespace('song', description="A namespace for Song")

class Song(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"))

    def __repr__(self):
        return f"<Song {self.name} >"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name):
        self.name=name
        db.session.commit()

class Playlist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    songs = db.relationship(
        "Song", 
        backref = "playlist",
        cascade = "all, delete, delete-orphan",
        single_parent = True
    )

    def __repr__(self):
        return f"<Playlist {self.name} >"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name):
        self.name=name
        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), nullable = False, unique = True)
    email = db.Column(db.String(80), nullable = False)
    password = db.Column(db.Text(), nullable = False)

    def __repr__(self):
        return f"<User {self.username}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()


song_model = songs_ns.model(
    "Song",
    {
       "id":fields.Integer(),
       "name":fields.String(),
       "playlist_id":fields.Integer()
    }
)

playlist_model = playlist_ns.model(
     "Playlist",
     {
        "id":fields.Integer(), 
        "name":fields.String(),
        "songs":fields.List(fields.Nested(song_model))
     }
)

signup_model = auth_ns.model(
    "SignUp",
    {
        "username":fields.String(),
        "email":fields.String(),
        "password":fields.String()
    }
)

login_model=auth_ns.model(
    "Login",
    {
        "username":fields.String(),
        "password":fields.String()
    }
)


