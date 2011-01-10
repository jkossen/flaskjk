# -*- coding: utf-8 -*-

"""
    flaskjk.helpers
    ~~~~~~~~~~~~~~~~~

    Generic helper functions

    :copyright: (c) 2010 by Jochem Kossen.
    :license: BSD, see LICENSE for more details.
"""

from unicodedata import normalize

import bcrypt
import os
import re

def encrypt_password(seed, password):
    """Encrypt given password using seed as an extra salt"""
    return bcrypt.hashpw('%s%s' % (seed, password), bcrypt.gensalt())

def validate_password(seed, password, hash):
    """Validation function for blowfish encrypted password"""
    return bcrypt.hashpw('%s%s' % (seed, password), hash) == hash

def slugify(text, delim=u'-', maxlen=128):
    """Generates an ASCII-only slug usable in paths and URLs.

    Based on http://flask.pocoo.org/snippets/5/

    """
    punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')
    result = []
    for word in punct_re.split(text.lower()):
        word = normalize('NFKD', unicode(word)).encode('ascii', 'ignore')
        if word:
            result.append(word)

    return unicode(delim.join(result)[0:maxlen])

def summarize(text, length=250, suffix='...'):
    """Generate summary from given string of text

    Based on http://stackoverflow.com/questions/250357/smart-truncate-in-python

    """
    if len(text) <= length:
        return text

    return text[:length+1].rsplit(' ', 1)[0]+suffix

