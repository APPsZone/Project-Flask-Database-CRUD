from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """ User Management """
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    
    def __init__ (self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username

class Jasa(db.Model):
    """Jasa Servis """
    __tablename__="jasaservis"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(60), nullable=False)
    harga = db.Column(db.String(256), nullable=False)
    
    def __init__ (self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def __repr__(self):
        return '<Jasa %r>' % self.nama

class Part(db.Model):
    """Spare Part """
    __tablename__="sparepart"
    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String(30), nullable=False)
    harga = db.Column(db.String(256), nullable=False)
    stok = db.Column(db.String(256), nullable=False)
    
    def __init__ (self, part, harga, stok):
        self.part = part
        self.harga = harga
        self.stok = stok
    
    def __repr__(self):
        return '<Part %r>' % self.part

class Aksesoris(db.Model):
    """ Aksesoris """
    __tablename__="aksesoris"
    id = db.Column(db.Integer, primary_key=True)
    namabarang = db.Column(db.String(30), nullable=False)
    harga = db.Column(db.String(256), nullable=False)
    stok = db.Column(db.String(256), nullable=False)
    
    def __init__ (self, namabarang, harga, stok):
        self.namabarang = namabarang
        self.harga = harga
        self.stok = stok
    
    def __repr__(self):
        return '<Aksesoris %r>' % self.namabarang
    
        
