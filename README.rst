=============================
Flaskjk
=============================
:Author: Jochem Kossen

Flaskjk_ is a Python_ library with generic code the author uses in his Flask_ based
projects. It contains, among other things, a Viewer class to deal with views in
a generic manner, and contains markup converter functions for ReST_ and
Markdown_.

Copyright and license
---------------------

:copyright: (c) 2010 by Jochem Kossen <jochem.kossen@gmail.com>
:license: two-clause BSD

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

   1. Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

helpers.py
~~~~~~~~~~
def hashify(seed, text):
    Generate sha256 hash from a concatenation of seed and string.

def slugify(text, delim=u'-', maxlen=128):
    Generates an ASCII-only slug usable in paths and URLs.

def summarize(text, length=250, suffix='...'):
    Generate summary from given string of text.

markup.py
~~~~~~~~~
def markup_to_html(format, text):
    Convert supported marked-up input to HTML output.

    Currently supported formats are 'rest' and 'markdown'.

restconverter.py
~~~~~~~~~~~~~~~~
class HTMLFragmentTranslator
    A docutils HTMLTranslator based class used for converting ReST input to HTML output.

def rest_to_html(s):
    Helper function to convert given ReST input string s to HTML output

viewer.py
~~~~~~~~~
class Viewer
    def view(self, rule, options):
        Decorator function for views. It basically binds a Flask/Werkzeug route
        to the decorated function

    def render(self, template, options):
        Render the given template

    def static(self, filename):
        Send the given file to the client, used for stylesheets, javascript, etc.

.. _Python: http://www.python.org
.. _Flask: http://flask.pocoo.org
.. _ReST: http://docutils.sourceforge.net/rst.html
.. _Markdown: http://daringfireball.net/projects/markdown
.. _Flaskjk: http://github.com/jkossen/flaskjk
