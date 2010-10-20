# -*- coding: utf-8 -*-
"""
    flaskjk.viewer
    ~~~~~~~~~~~~~~

    Viewer class to generalize views

    :copyright: (c) 2010 by Jochem Kossen.
    :license: BSD, see LICENSE for more details.
"""

from flask import render_template, send_from_directory
import os

class Viewer(object):
    """Class to handle views (as in Model/View/Controller)"""
    def __init__(self, app, template_path):
        super(Viewer, self).__init__()
        self.app = app
        self.template_path = template_path
        self.static_path = os.path.join(app.root_path, 'templates', template_path, app.config['THEME'], 'static')

    def view(self, rule, **options):
        """ Decorator for views """
        complete_rule = '/%s%s' % (self.app.config['PREFIX'], self.app.config['ROUTES'][rule])

        def decorator(f):
            self.app.add_url_rule(complete_rule, None, f, **options)
            return f
        return decorator

    def render(self, template, **options):
        """ Render template from a configured subdir to implement themes """
        template_path = os.path.join(self.template_path, self.app.config['THEME'], template)
        return render_template(template_path, **options)

    def static(self, filename):
        """Send static files such as style sheets, JavaScript, etc."""
        return send_from_directory(self.static_path, filename)
