# -*- coding: utf-8 -*-

try:
    import httplib
except ImportError:
    import http.client as httplib

from expects.matchers import Matcher
from expects.matchers.built_in import have_key, have_keys


class _be_ok(Matcher):
    def _match(self, response):
        return response.code < httplib.BAD_REQUEST


class _be_json(Matcher):
    def _match(self, response):
        return 'application/json' in response.headers['Content-Type']


class have_header(have_key):
    def _match(self, response):
        return super(have_header, self)._match(response.headers)

    def _description(self, response):
        return super(have_header, self)._description(response.headers)


class have_headers(have_keys):
    def _match(self, response):
        return super(have_headers, self)._match(response.headers)

    def _description(self, response):
        return super(have_headers, self)._description(response.headers)


class have_status(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, response):
        return response.code == self._expected

be_ok = _be_ok()
be_json = _be_json()

__all__ = ['be_ok', 'be_json', 'have_header', 'have_headers', 'have_status']
