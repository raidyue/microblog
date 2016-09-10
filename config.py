# encoding=utf-8
import os
BASE_DIR = os.path.abspath(os.path.dirname(__name__))

CSRF_ENABLED = True
SECRET_KEY = 'what-the-fuck'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

# db
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
