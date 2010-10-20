# -*- coding: utf-8 -*-

"""
    flaskjk.helpers
    ~~~~~~~~~~~~~~~~~

    Generic helper functions

    :copyright: (c) 2010 by Jochem Kossen.
    :license: BSD, see LICENSE for more details.
"""

from hashlib import sha256
from unicodedata import normalize

import os
import re

def hashify(seed, text):
    """Generate sha256 hash from a concatenation of seed and string"""

    return sha256('%s%s' % (seed, text)).hexdigest()

def slugify(text, delim=u'-', maxlen=128):
    """Generates an ASCII-only slug usable in paths and URLs.

    Based on http://flask.pocoo.org/snippets/5/

    """
    punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
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

