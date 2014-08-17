# -*- coding: utf-8 -*-

import httplib

from expects.matchers import Matcher


class _be_ok(Matcher):
    def _match(self, response):
        return response.code < httplib.BAD_REQUEST


class _be_json(Matcher):
    def _match(self, response):
        return 'application/json' in response.headers['Content-Type']

be_json = _be_json()

be_ok = _be_ok()
be_json = _be_json()

__all__ = ['be_ok', 'be_json']
