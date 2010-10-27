# -*- coding: utf-8 -*-

"""
    flaskjk.markup
    ~~~~~~~~~~~~~~

    Functions for converting between document formats.

    Currently the formats ReST (ReStructuredText) and Markdown are supported.

    :copyright: (c) 2010 by Jochem Kossen.
    :license: BSD, see LICENSE for more details.
"""

from .restconverter import rest_to_html
from markdown import markdown
import re

def markup_to_html(format, text):
    """Convert supported marked-up input to HTML output"""
    if format.value == 'rest':
        return rest_to_html(text)
    elif format.value == 'markdown':
        return markdown(text)

    return text

def multi_replace(subject, repl_map):
    """ replace all occurrences of repl_map.keys by their values """
    rc = re.compile('|'.join(map(re.escape, repl_map)))
    def translate(match):
        return repl_map[match.group(0)]
    return rc.sub(translate, subject)

