import os
from flask import Flask
from flask_ask import Ask, statement
from gmusicapi import Mobileclient

app = Flask(__name__)
email = os.environ.get('email', 17995)
password = os.environ.get('password', 17995)
android_id = os.environ.get('android_id', 17995)

ask = Ask(app, '/alexa')

client = Mobileclient()

print('Logging in as:', email, 'with ANDROID_ID', android_id)

if client.login(email, password, android_id):
    print('Login successful!')
else:
    raise Exception('Login failed')

from . import utils
musicman = utils.musicmanager.MusicManager(client)
music_queue = utils.queue.MusicQueue()

from . import intents
