# -*- coding: utf-8 -*-

"""
    flaskjk.restconverter
    ~~~~~~~~~~~~~~~~~~~~~

    Helper functions for converting RestructuredText

    This class heavily depends on the functionality provided by the docutils
    package.

    :copyright: (c) 2010 by Jochem Kossen.
    :license: BSD, see LICENSE for more details.
"""

from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator

class HTMLFragmentTranslator(HTMLTranslator):
    def __init__(self, document):
        HTMLTranslator.__init__(self, document)
        self.head_prefix = ['','','','','']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []
        def astext(self):
            return ''.join(self.body)

html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator

def rest_to_html(s):
    """Convert ReST input to HTML output"""
    return core.publish_string(s, writer=html_fragment_writer)

