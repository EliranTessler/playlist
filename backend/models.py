from exts import db
from sqlalchemy import ForeignKey

class Song(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    playlist_id=db.Column(db.Integer, db.ForeignKey("playlist.id"))

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
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    songs=db.relationship(
        "Song", 
        backref="playlist",
        cascade="all, delete, delete-orphan",
        single_parent=True
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
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False, unique=True)
    email=db.Column(db.String(80), nullable=False)
    password=db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"