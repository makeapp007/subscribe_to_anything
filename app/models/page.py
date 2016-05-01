from flask.ext.login import UserMixin
from app import db

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    name = db.Column(db.Text)
    url = db.Column(db.Text)
    postdata = db.Column(db.Text)
    ua = db.Column(db.Text)
    referer = db.Column(db.Text)
    cookie = db.Column(db.Text)
    method = db.Column(db.Enum('GET','POST'))
    watch_type = db.Column(db.Enum('change','keyword'))
    notify_content = db.Column(db.Enum('diff','new','all'))
    freq = db.Column(db.Integer)
    user = db.relationship('User',backref=db.backref('pages'))

    def __init__(self,name,url,postdata,ua,referer,cookie,method,watch_type,notify_content,freq,user):
        self.name=name
        self.url=url
        self.postdata=postdata
        self.ua=ua
        self.referer=referer
        self.cookie=cookie
        self.method=method
        self.watch_type=watch_type
        self.notify_content=notify_content
        self.freq=freq
        self.user=user

    def save(self):
        db.session.add(self)
        db.session.commit()
