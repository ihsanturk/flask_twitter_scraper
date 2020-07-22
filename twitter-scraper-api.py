#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
import sys
from twitter_scraper import get_tweets
from twitter_scraper import Profile
import json
import datetime
import random
import string
import logging
import json
import httplib2
import requests

app = Flask(__name__)

def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

# profile
@app.route('/api/profile')
def profile():
    user = request.args.get('user', default = 'crypto_rand', type = str)
    return json.dumps(Profile(user).to_dict(), default=default)

# tweets
@app.route('/api/tweets')
def tweets():
    pages = request.args.get('pages', default = 1, type = int)
    user = request.args.get('user', default = 'crypto_rand', type = str)
    userTweets = []
    for tweet in get_tweets(user, pages):
        userTweets.append(tweet)
    return json.dumps(userTweets, default=default)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
