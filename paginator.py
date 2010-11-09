from flask import url_for, abort
from werkzeug import cached_property

# Paginator class {{{
class Paginator(object):
    def __init__(self, items, per_page, page, endpoint, **kwargs):
        self.items = items
        self.per_page = per_page
        self.page = page
        self.endpoint = endpoint
        self.extra_args = {}
        for key in kwargs:
            self.extra_args[key] = kwargs[key]

        if (self.page > self.pages or self.page < 1):
            abort(404)

    @cached_property
    def count(self):
        return self.items.count()

    @cached_property
    def entries(self):
        offset = (self.page - 1) * self.per_page
        end = offset + self.per_page
        return self.items[offset:end]

    has_previous = property(lambda x: x.page > 1)
    has_next = property(lambda x: x.page < x.pages)
    previous = property(lambda x: url_for(x.endpoint, page=x.page - 1, **x.extra_args))
    next = property(lambda x: url_for(x.endpoint, page=x.page + 1, **x.extra_args))
    first = property(lambda x: url_for(x.endpoint, page=1, **x.extra_args))
    last = property(lambda x: url_for(x.endpoint, page=x.pages, **x.extra_args))
    pages = property(lambda x: max(0, x.count - 1) // x.per_page + 1)
# }}}

