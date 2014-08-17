# -*- coding: utf-8 -*-

try:
    import httplib
except ImportError:
    import http.client as httplib

from expects.matchers import Matcher


class _be_ok(Matcher):
    def _match(self, response):
        return response.code < httplib.BAD_REQUEST


class _be_json(Matcher):
    def _match(self, response):
        return 'application/json' in response.headers['Content-Type']


class have_header(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, response):
        return self._expected in response.headers

be_ok = _be_ok()
be_json = _be_json()

__all__ = ['be_ok', 'be_json', 'have_header']
