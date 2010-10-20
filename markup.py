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
import markdown.markdown

def markup_to_html(format, text):
    """Convert supported marked-up input to HTML output"""
    if format.value == 'rest':
        return rest_to_html(text)
    elif format.value == 'markdown':
        return markdown(text)

    return text


