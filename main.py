#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import random

from flask import Flask, request, redirect

import combos

app = Flask(__name__)

def valid_link_from(dirty_link):
    link = urllib2.unquote(dirty_link)

    if urllib2.urlparse.urlparse(link).scheme is '':
        link = 'http://' + link
    
    try:
        req = urllib2.Request(link)
        req.get_method = lambda:'HEAD'
        response = urllib2.urlopen(req)
        
        if response.getcode() >= 400:
            return None
    except urllib2.URLError:
        return None

    return link

@app.route('/shorten', methods=['POST'])
def shorten():
    link = valid_link_from(request.args['link'])
        
    if link:
        combo = combos.create_unique()

        combos.add_link(link, combo)
        
        return combo, 201, {'Content-Type' : 'text/plain'}
    else:
        return "No link given.", 400

@app.route('/<combo>', methods=['GET'])
def visit(combo):
    if combos.has(combo):
        return redirect(combos.link_for(combo), 301)
    else:
        return "No url for the given combo.", 404

if __name__ == "__main__":
    app.run()
